import argparse
import grpc
import importlib.util
import inspect
import json
import os
import sys

from gRPC.proto_common import pts_trigger_pb2, pts_trigger_pb2_grpc
from Utils.logger import Logger
# Initialize logger
logger = Logger().logger

# Setup paths
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def load_testbed(config_path):
    """Loads and parses the testbed configuration from a JSON file.

    Args:
        config_path: Path to the testbed JSON config file.

    Returns:
        dict: Parsed JSON data.
    """
    logger.info("Loading testbed configuration from: %s", config_path)
    if not os.path.exists(config_path):
        logger.error("Config file not found: %s", config_path)
        sys.exit(1)
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error("JSON parse error: %s", str(e))
        sys.exit(1)


def validate_testbed(testbed_data, testbed_name):
    """Validates the given testbed name and extracts IP and MAC addresses.

    Args:
        testbed_data: Parsed testbed configuration.
        testbed_name: Name of the testbed to validate.

    Returns:
        dict: Dictionary of devices with 'ip' and 'mac' keys.
    """
    logger.info("Validating testbed: %s", testbed_name)

    try:
        if testbed_name not in testbed_data:
            raise ValueError(f"Testbed '{testbed_name}' not found in config.")
        tb = testbed_data[testbed_name]
        device_map = {}
        for dev_name, dev_info in tb.items():
            host_ip = dev_info.get("host_ip")
            bd_address = dev_info.get("bd_address")
            if not host_ip or not bd_address:
                raise ValueError(f"Missing IP or MAC for {dev_name}")
            device_map[dev_name] = {
                "ip": host_ip,
                "mac": bd_address
            }
        logger.info("Parsed devices from testbed:")
        for name, info in device_map.items():
            logger.info(f"{name}: IP={info['ip']}, MAC={info['mac']}")
        return device_map
    except Exception as e:
        logger.error("Error validating config.json: %s", str(e))
        sys.exit(1)


def load_test_module(module_name):
    """Dynamically loads a test module from the 'testcases' directory.

    Args:
        module_name: Name of the test module (without '.py').

    Returns:
        module: The loaded Python module object.
    """
    logger.info("Loading test module: testcases.%s", module_name)
    module_path = os.path.join(project_root, "testcases", f"{module_name}.py")
    if not os.path.exists(module_path):
        logger.error("Module file not found at: %s", module_path)
        sys.exit(1)
    try:
        spec = importlib.util.spec_from_file_location(f"testcases.{module_name}", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        logger.error("Failed to load module '%s': %s", module_name, str(e))
        sys.exit(1)


def get_test_function(module, function_name):
    """
    Retrieves the test function or class method by name.

    Args:
        module (module): Loaded Python module.
        function_name (str): Name of the function or method to execute.

    Returns:
        tuple: (function, instance) where instance is None for standalone functions.

    Raises:
        SystemExit: If the function is not found.
    """
    if hasattr(module, function_name):
        logger.info("Found function '%s' directly in module", function_name)
        return getattr(module, function_name), None
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if hasattr(obj, function_name):
            logger.info("Found function '%s' inside class '%s'", function_name, name)
            instance = obj()
            method = getattr(instance, function_name)
            return method, instance
    logger.error("Function '%s' not found in module '%s'", function_name, module.__name__)
    sys.exit(1)


def run_test(test_func, devices, audio_filepath, config_path, testbed_name):
    """
    Executes the test function with dynamically resolved arguments.

    Args:
        test_func (function): The test function to call.
        devices (dict): Parsed devices with IP/MAC.
        audio_filepath (str): Path to audio file.
        config_path (str): Path to the config file.
        testbed_name (str): Name of the testbed.

    Raises:
        SystemExit: If the test function fails.
    """
    logger.info("Executing test: %s", test_func.__name__)

    try:
        sig = inspect.signature(test_func)
        args = sig.parameters
        kwargs = {}
        # Only pass arguments required by the test function
        if "devices" in args:
            kwargs["devices"] = devices
        if "audio_filepath" in args:
            kwargs["audio_filepath"] = audio_filepath
        if "config_path" in args:
            kwargs["config_path"] = config_path
        if "testbed_name" in args:
            kwargs["testbed_name"] = testbed_name
        if "dut_ip" in args:
            kwargs["dut_ip"] = devices.get("dut1", {}).get("ip")
        if "ref_ip" in args:
            kwargs["ref_ip"] = devices.get("ref1", {}).get("ip")
        if "dut_mac" in args:
            kwargs["dut_mac"] = devices.get("dut1", {}).get("mac")
        if "ref_mac" in args:
            kwargs["ref_mac"] = devices.get("ref1", {}).get("mac")
        if "target_mac" in args:
            first_ref = next((k for k in devices if k.startswith("ref")), None)
            if first_ref:
                kwargs["target_mac"] = devices[first_ref]["mac"]

        logger.info(f"Passing arguments to test function: {kwargs}")
        test_func(**kwargs)
        logger.info("Test completed successfully.")
    except Exception as e:
        logger.error("Test function '%s' raised an error:\n%s", test_func.__name__, str(e))
        sys.exit(1)

def run_pts_trigger(args):

    logger.info("Triggering PTS project via gRPC")

    config_data = load_testbed(args.config)
    controller_ip = config_data.get("controller_ip")

    channel = grpc.insecure_channel(f"{controller_ip}:50051")
    stub = pts_trigger_pb2_grpc.PTSTriggerStub(channel)
    request = pts_trigger_pb2.ProjectRequest(
        config=args.config,
        testbed=args.testbed,
        workspace=args.workspace,
        project=args.project,
    )
    for output in stub.RunProject(request):
        logger.info(output.line)
    download_report(stub, args)
    logger.info("PTS execution completed")

def download_report(stub, args):
    logger.info("Downloading PTS report from server...")
    request = pts_trigger_pb2.ProjectRequest(
        config=args.config,
        testbed=args.testbed,
        workspace=args.workspace,
        project=args.project,
    )
    report = stub.GetReport(request)
    save_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, report.filename)
    with open(save_path, "wb") as f:
        f.write(report.content)
    logger.info("Report saved at: %s", save_path)

def parse_args():
    """Parse command line arguments for the  gRPC client.

    This client supports two commands:
      - run_test: Execute Bluetooth test cases locally.
      - pts_trigger: Trigger PTS test execution remotely via gRPC.

    Returns:
        Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Unified Bluetooth & PTS gRPC Client")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_test_parser = subparsers.add_parser("run_test", help="Run Bluetooth testcases")
    run_test_parser.add_argument("--module", required=True)
    run_test_parser.add_argument("--function", required=True)
    run_test_parser.add_argument("--config", required=True)
    run_test_parser.add_argument("--testbed", default="testbed_a2dp")
    run_test_parser.add_argument(
        "--audio_file",
        default="/root/Downloads/a2dp_grpc_testing.wav"
    )
    pts_parser = subparsers.add_parser("pts_trigger", help="Trigger PTS test execution")
    pts_parser.add_argument("--config", required=True)
    pts_parser.add_argument("--testbed", required=True)
    pts_parser.add_argument("--workspace", required=True)
    pts_parser.add_argument("--project", required=True)
    return parser.parse_args()


def main():
    """Entry point for the gRPC client application.

    Based on the chosen command, this function either:
      - Executes a Bluetooth test locally (run_test), or
      - Triggers a remote PTS test via gRPC (pts_trigger).
    """
    logger.info("==============================")
    logger.info("gRPC Client Started")
    logger.info("==============================")
    args = parse_args()
    if args.command == "run_test":
        testbed_data = load_testbed(args.config)
        devices = validate_testbed(testbed_data, args.testbed)
        module = load_test_module(args.module)
        test_func, _ = get_test_function(module, args.function)
        run_test(
            test_func,
            devices=devices,
            audio_filepath=args.audio_file,
            config_path=args.config,
            testbed_name=args.testbed
        )
    elif args.command == "pts_trigger":
        run_pts_trigger(args)

if __name__ == "__main__":
    main()



