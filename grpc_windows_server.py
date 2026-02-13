import argparse
import json
import os
import subprocess
import time
from getpass import getpass
from concurrent import futures
import logging
import grpc
import queue
import threading
from pts_report import generate_pts_table_report
from Utils.logger import Logger
from gRPC.proto_common import pts_trigger_pb2, pts_trigger_pb2_grpc
from testcases.pts.pts_gap_tests import gap_testcases
from testcases.pts.a2dp import a2dp_testcases
from libraries.pts.pts_grpc_executor import execute_test
from libraries.pts.pts_windows_server import PTSController

logger = Logger().logger


class GRPCDeployer:
    """A class to automate the deployment of gRPC server and client scripts on multiple remote machines over SSH.

    This includes:
    - Copying source code to target systems
    - Ensuring passwordless SSH setup
    - Launching gRPC server/client in remote terminals
    """

    remote_user = "root"
    """Default SSH username for remote machines."""
    ssh_key_path = os.path.expanduser("~/.ssh/id_rsa")
    """Default path to the SSH private key used for authentication."""

    def __init__(self, config_path, testcase_file, test_function, testbed_name, remote_dir="~/test_deploy"):
        """Initialize the GRPCDeployer with configuration and test case information.

        Args:
            config_path: Path to the config.json file.
            testcase_file: Path to the test case file to be executed.
            test_function: Test function name to run.
            testbed_name: Name of the testbed to use from the config file.
            remote_dir: Remote directory where files will be copied. Defaults to "~/test_deploy".
        """
        self.config_path = config_path
        self.testcase_file = testcase_file
        self.test_function = test_function
        self.testbed_name = testbed_name
        self.remote_dir = remote_dir
        self.testbed_data = self.load_json(self.config_path)
        if testbed_name not in self.testbed_data:
            raise ValueError(f"Testbed '{testbed_name}' not found in config.json")
        self.testbed_config = self.testbed_data[testbed_name]
        self.client_ip = self.testbed_data["controller_ip"]
        self.dut_ip = self.testbed_config["dut1"]["host_ip"]
        self.ref_ips = [v["host_ip"] for k, v in self.testbed_config.items() if k.startswith("ref")]
        self.server_ips = [self.dut_ip] + self.ref_ips
        self.client_ips = [self.client_ip]
        self.all_unique_ips = list(set(self.server_ips + self.client_ips))
        logger.info(f"Client ip is : {self.client_ips}")

    def load_json(self, json_file):
        """Load and return contents of a JSON file.

        Args:
            json_file: Path to the JSON file.

        Returns:
            Parsed JSON content.
        """
        with open(json_file) as f:
            return json.load(f)

    def ensure_ssh_key(self):
        """Ensure that an SSH key exists. If not, generates a new SSH key pair."""
        if not os.path.exists(self.ssh_key_path):
            logger.info("Generating SSH key...")
            subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "2048", "-f", self.ssh_key_path, "-N", ""])

    def ensure_passwordless_ssh(self, ip):
        """Ensure passwordless SSH access is set up for the given IP.

        Args:
            ip: IP address of the remote host.
        """
        logger.info(f"[{ip}]  Checking passwordless SSH access...")
        test_cmd = subprocess.run(
            ["ssh", "-i", self.ssh_key_path, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no",
             f"{self.remote_user}@{ip}", "echo 1"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if test_cmd.returncode != 0:
            self.ensure_ssh_key()
            password = getpass(f"Enter password for {self.remote_user}@{ip}: ")
            subprocess.run(
                ["sshpass", "-p", password, "ssh-copy-id", "-i", f"{self.ssh_key_path}.pub", f"{self.remote_user}@{ip}"],
                check=True
            )
            logger.info(f"[{ip}] SSH key successfully copied.")

    def ssh_command(self, ip, command):
        """Run a command via SSH on a remote machine.

        Args:
            ip: IP address of the remote machine.
            command: Command to execute.

        Returns:
            True if command executed successfully, else False.
        """
        self.ensure_passwordless_ssh(ip)
        ssh_cmd = ["ssh", "-i", self.ssh_key_path, "-o", "StrictHostKeyChecking=no", f"{self.remote_user}@{ip}", command]
        logger.info(f"[{ip}]  SSH CMD: {command}")
        proc = subprocess.run(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode().strip()
        err = proc.stderr.decode().strip()
        if out: logger.info(f"[{ip}]  SSH STDOUT:\n{out}")
        if err: logger.info(f"[{ip}]  SSH STDERR:\n{err}")
        return proc.returncode == 0

    def scp_directory(self, ip, local_dir, remote_dir):
        """Securely copy a local directory to a remote host.

         Args:
             ip: IP address of the remote machine.
             local_dir: Path to the local directory.
             remote_dir: Path on the remote machine.

         Returns:
             True if copied successfully, else False.
         """
        self.ensure_passwordless_ssh(ip)
        self.ssh_command(ip, f"mkdir -p {remote_dir}")
        cmd = ["scp", "-i", self.ssh_key_path, "-r", "-o", "StrictHostKeyChecking=no",
               local_dir, f"{self.remote_user}@{ip}:{remote_dir}"]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            logger.info(f"[{ip}] SCP failed: {proc.stderr.decode().strip()}")
            return False
        return True

    def deploy_files(self, ip):
        """Deploy test scripts and utilities to a remote host.

        Args:
            ip: IP address of the remote machine.

        Returns:
            True if deployment succeeded, else False.
        """
        base_dir = os.path.abspath(os.path.dirname(__file__))
        test_automation_path = os.path.abspath(base_dir)
        if not self.scp_directory(ip, test_automation_path, self.remote_dir):
            return False
        self.ssh_command(ip, f"chmod -R +x {self.remote_dir}")
        return True

    def launch_server(self, ip):
        """Launch gRPC server script on the remote device in a new terminal window.

        Args:
            ip: IP address of the server.
        """
        script_path = f"{self.remote_dir}/test_automation/server.py"
        title = f"gRPC-SERVER-{ip}"
        cmd = (
            f'DISPLAY=:0 gnome-terminal --title="{title}" -- bash -c '
            f'"echo Starting gRPC Server on {ip}; '
            f'DBUS_SYSTEM_BUS_ADDRESS=unix:path=/var/run/dbus/system_bus_socket '
            f'python3 {script_path}; exec bash"'
        )
        logger.info((f"[{ip}]  Starting SERVER in gnome-terminal..."))
        self.ssh_command(ip, cmd)

    def launch_client(self, ip):
        """Launch gRPC client script on the controller machine in a new terminal window.

        Args:
            ip: IP address of the client/controller.
        """
        test_module = os.path.splitext(os.path.basename(self.testcase_file))[0]
        script_path = f"{self.remote_dir}/test_automation/client.py"
        config_path = f"{self.remote_dir}/test_automation/config.json"
        cmd = (
            f'DISPLAY=:0 gnome-terminal --title="gRPC-CLIENT-{ip}" -- bash -c '
            f'"echo Starting gRPC Client on {ip}; '
            f'DBUS_SYSTEM_BUS_ADDRESS=unix:path=/var/run/dbus/system_bus_socket '
            f'python3 {script_path} --module {test_module} '
            f'--function {self.test_function} --testbed {self.testbed_name} '
            f'--config {config_path}; exec bash"'
        )
        self.ssh_command(ip, cmd)

    def run(self):
        """Perform the full deployment process across all machines:
        - Deploy files
        - Launch servers
        - Launch clients
        """
        for ip in self.all_unique_ips:
            if not self.deploy_files(ip):
                continue
        time.sleep(5)
        for ip in self.server_ips:
            self.launch_server(ip)
        time.sleep(5)
        for ip in self.client_ips:
            self.launch_client(ip)


class GRPCLogBridge(logging.Handler):
    """Logging handler that captures log messages into an in-memory queue.

    This is used to bridge normal Python logging output into
    the gRPC streaming response so that logs can be sent back
    to the client line-by-line.
    """

    def __init__(self):
        """Initialize the log bridge with an empty message queue."""
        super().__init__()
        self.queue = []

    def emit(self, record):
        """Capture a log record and store the formatted message.

        Args:
            record: Log record emitted by the logger.
        """
        try:
            message = self.format(record)
            self.queue.append(message)
        except Exception:
            pass


def load_testcases(project):
    """Return the list of PTS testcases for a given project.

    Args:
        project : PTS project name (e.g., "GAP").

    Returns:
        List of testcase identifiers for the project.
    """
    if project == "GAP":
        return gap_testcases
    elif project == "A2DP":
        return a2dp_testcases
    raise ValueError(f"Unknown project {project}")


class PTSTriggerService(pts_trigger_pb2_grpc.PTSTriggerServicer):
    """gRPC service that triggers PTS test execution.

    This service receives test parameters over gRPC, launches the
    PTS runner as a subprocess, and streams the test output back
    to the client line by line.
    """

    def RunProject(self, request, context):
        """Execute all PTS testcases and stream logs + summary to both Windows and Linux."""

        results = []
        pass_count = 0
        fail_count = 0
        inconclusive_count = 0
        log_bridge = GRPCLogBridge()
        log_bridge.setFormatter(logging.Formatter("%(message)s"))
        #logger.addHandler(log_bridge)
        if log_bridge not in logger.handlers:
            logger.addHandler(log_bridge)

        try:
            start_msg = f"Starting project execution: {request.project}"
            logger.info(start_msg)
            yield pts_trigger_pb2.TestOutput(line=start_msg)
            project_testcases = load_testcases(request.project)
            load_msg = f"Loaded {len(project_testcases)} testcases for {request.project}"
            logger.info(load_msg)
            yield pts_trigger_pb2.TestOutput(line=load_msg)
            for index, testcase_name in enumerate(project_testcases, 1):
                run_msg = f"===== [{index}/{len(project_testcases)}] Running {testcase_name} ====="
                logger.info(run_msg)
                yield pts_trigger_pb2.TestOutput(line=run_msg)
                pts, verdict, reason = execute_test(
                    config=request.config,
                    testbed=request.testbed,
                    workspace=request.workspace,
                    project=request.project,
                    testcase=testcase_name,
                    logger=logger,
                )
                if verdict == "PASS":
                    pass_count += 1
                elif verdict == "FAIL":
                    fail_count += 1
                else:
                    inconclusive_count += 1
                results.append({
                    "testcase": testcase_name,
                    "verdict": verdict,
                    "reason": reason
                })
                for log_line in log_bridge.queue:
                    yield pts_trigger_pb2.TestOutput(line=log_line)
                log_bridge.queue.clear()
                done_msg = f"{testcase_name} DONE"
                logger.info(done_msg)
                yield pts_trigger_pb2.TestOutput(line=done_msg)
            total = len(results)
            logger.info("")
            logger.info("==============================")
            logger.info("PTS EXECUTION SUMMARY")
            logger.info("==============================")
            yield pts_trigger_pb2.TestOutput(line="")
            yield pts_trigger_pb2.TestOutput(line="==============================")
            yield pts_trigger_pb2.TestOutput(line="PTS EXECUTION SUMMARY")
            yield pts_trigger_pb2.TestOutput(line="==============================")
            for r in results:
                if r["verdict"] == "PASS":
                    summary_line = f"{r['testcase']} : PASS"
                else:
                    reason = r["reason"] or "No failure reason provided"
                    summary_line = f"{r['testcase']} : {r['verdict']} : {reason}"
                logger.info(summary_line)
                yield pts_trigger_pb2.TestOutput(line=summary_line)
            logger.info("------------------------------")
            yield pts_trigger_pb2.TestOutput(line="------------------------------")
            logger.info(f"Total testcases : {total}")
            logger.info(f"Passed          : {pass_count}")
            logger.info(f"Failed          : {fail_count}")
            logger.info(f"Inconclusive    : {inconclusive_count}")
            yield pts_trigger_pb2.TestOutput(line=f"Total testcases : {total}")
            yield pts_trigger_pb2.TestOutput(line=f"Passed          : {pass_count}")
            yield pts_trigger_pb2.TestOutput(line=f"Failed          : {fail_count}")
            yield pts_trigger_pb2.TestOutput(line=f"Inconclusive    : {inconclusive_count}")
            generate_pts_table_report(
                project=request.project,
                results=results,
                output_dir="reports"
            )

            logger.info("==============================")
            yield pts_trigger_pb2.TestOutput(line="==============================")
            logger.info("Stopping PTS server")
            PTSController.stop_pts_server(self, logger)
            finish_msg = "Project execution finished"
            logger.info(finish_msg)
            yield pts_trigger_pb2.TestOutput(line=finish_msg)
        except Exception as error:
            error_msg = f"Project failed: {str(error)}"
            logger.error(error_msg)
            yield pts_trigger_pb2.TestOutput(line=error_msg)
        finally:
            logger.removeHandler(log_bridge)

    def GetReport(self, request, context):

        report_dir = os.path.join(os.getcwd(), "reports")

        latest_file = max(
            [os.path.join(report_dir, f) for f in os.listdir(report_dir)],
            key=os.path.getctime
        )

        with open(latest_file, "rb") as f:
            content = f.read()

        return pts_trigger_pb2.ReportFile(
            filename=os.path.basename(latest_file),
            content=content
        )


def serve():
    """Start the PTS Trigger gRPC server.

    This function initializes the gRPC server, registers the
    PTSTriggerService, starts listening on port 50051, and blocks until the server is terminated.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pts_trigger_pb2_grpc.add_PTSTriggerServicer_to_server(PTSTriggerService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logger.info("PTS Server running on port 50051")
    server.wait_for_termination()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['deploy', 'pts'], default='pts',
                        help="Run deployer or pts server")
    parser.add_argument('-c', '--config', help="Path to config.json")
    parser.add_argument('-f', '--file', help="Testcase filename")
    parser.add_argument('--function', help="Test function name")
    parser.add_argument('--testbed', help="Testbed name")
    parser.add_argument('-r', '--remote_dir', default="~/test_deploy")
    args = parser.parse_args()
    if args.mode == 'pts':
        serve()
        return
    deployer = GRPCDeployer(
        config_path=args.config,
        testcase_file=args.file,
        test_function=args.function,
        testbed_name=args.testbed,
        remote_dir=args.remote_dir
    )
    deployer.run()

if __name__ == "__main__":
    main()