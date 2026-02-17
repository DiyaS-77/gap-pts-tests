import os

from Utils.logger import Logger
from Utils.utils import (
    start_bluetooth_daemon,
    start_dbus_daemon,
    start_pulseaudio_daemon,
    get_controllers_connected
)
from gRPC.proto_common import remote_pb2, remote_pb2_grpc
from libraries.bluetooth.bluez import BluetoothDeviceManager

logger = Logger().logger  # Get the logger instance


def convert_param(param):
    """
    Convert a string to int, float, bool, or return it as a string.

    Args:
        param (str): The input parameter as a string.

    Returns:
        Union[int, float, bool, str]: Converted parameter.
    """
    try:
        return int(param)
    except ValueError:
        pass
    try:
        return float(param)
    except ValueError:
        pass
    if param.lower() == "true":
        return True
    if param.lower() == "false":
        return False
    return param


class RemoteBluetoothProxy:
    """
    Client-side proxy that forwards Bluetooth commands to the server via gRPC.

    This class dynamically maps method calls to RPC requests using gRPC's CommandHandler.
    """

    def __init__(self, stub):
        """
        Initialize the proxy with a gRPC stub.

        Args:
            stub: gRPC stub for RemoteControlServicer.
        """
        self.stub = stub

    def __getattr__(self, method_name):
        """
        Dynamically map method names to gRPC commands.

        Args:
            method_name (str): Name of the method to call remotely.

        Returns:
            Callable: Function that sends a gRPC command with provided arguments.
        """
        def method(*args, **kwargs):
            parameters = [str(arg) for arg in args]
            metadata = {str(k): str(v) for k, v in kwargs.items()}
            request = remote_pb2.CommandRequest(
                command=method_name,
                parameters=parameters,
                metadata=metadata
            )
            response = self.stub.CommandHandler(request)

            if not response.success:
                error_msg = f"[gRPC] Command {method_name}: {response.error}"
                if logger:
                    logger.error(error_msg)

            return response.items if response.items else None

        return method


class RemoteControlServicer(remote_pb2_grpc.RemoteControlServicer):
    def __init__(self, log_path=None):
        """
        Initialize the gRPC server with logging and Bluetooth services.

        Args:
            log_path (str): Directory to store log files. If None, uses Logger().log_path.
        """
        Logger(subdir="linux")

        if log_path:
            os.makedirs(log_path, exist_ok=True)
            self.log_path = log_path
            setattr(logger, "log_path", log_path)
            Logger().setup_logger_file(log_path)
        else:
            self.log_path = getattr(logger, "log_path", None)
            if not self.log_path:
                self.log_path = Logger().logger.log_path
            os.makedirs(self.log_path, exist_ok=True)
            setattr(logger, "log_path", self.log_path)
        self.bt_manager = None
        self._setup_logging()
        self._init_bt_components()
        logger.info("[SERVER INIT] RemoteControlServicer initialized.")

    def _setup_logging(self):
        """
        Start system-level daemons required for Bluetooth operation.

        Starts D-Bus, Bluetoothd, and PulseAudio services.
        """
        start_dbus_daemon(logger)
        start_bluetooth_daemon(logger)
        start_pulseaudio_daemon(logger)

    def _init_bt_components(self):
        """
        Initialize Bluetooth manager and interface.

        Detects connected Bluetooth controllers and sets up the default interface.
        Registers an agent for pairing and communication.

        Raises:
            RuntimeError: If no Bluetooth controllers are found.
        """
        if self.bt_manager is None:
            logger.info("[INFO] Detecting Bluetooth interfaces...")
            controllers = get_controllers_connected(logger)
            if not controllers:
                raise RuntimeError("No Bluetooth controllers found.")

            # Select the first available controller (e.g., hci0)
            interface = next(iter(controllers.values()))
            logger.info("[INFO] Using interface: %s", interface)

            logger.info("[INFO] Initializing BluetoothDeviceManager...")
            self.bt_manager = BluetoothDeviceManager(log=logger, interface=interface)

            # Register the agent
            if self.bt_manager.register_agent(capability="DisplayYesNo"):
                logger.info("[AGENT] Registered agent with NoInputNoOutput capability.")
            else:
                logger.warning("[AGENT] Failed to register agent.")

    def CommandHandler(self, request, context):
        """
        Handle gRPC commands sent by clients.

        Dynamically invokes a method on the BluetoothDeviceManager instance
        based on the command name and parameters provided.

        Args:
            request (remote_pb2.CommandRequest): Contains the command name, parameters, and metadata.
            context: gRPC context object.

        Returns:
            remote_pb2.CommandResponse: Result of command execution, including status and any output items.
        """
        command = request.command
        parameters = request.parameters
        metadata = request.metadata

        try:
            logger.info("[SERVER] Received command: %s", command)
            logger.info("[SERVER] Parameters: %s", parameters)
            logger.info("[SERVER] Metadata: %s", metadata)

            method = getattr(self.bt_manager, command, None)
            if method is None:
                error_msg = f"Method '{command}' not found in BluetoothDeviceManager"
                logger.error(error_msg)
                return remote_pb2.CommandResponse(
                    success=False,
                    message="Method not found",
                    error=error_msg,
                    items=[]
                )

            converted_params = [convert_param(p) for p in parameters]
            logger.info("[SERVER] Invoking: %s (%s)", command, converted_params)

            result = method(*converted_params) if converted_params else method()

            items = []
            if result is not None:
                if isinstance(result, list):
                    items = [str(r) for r in result]
                else:
                    items = [str(result)]

            return remote_pb2.CommandResponse(
                success=True,
                message="OK",
                items=items
            )

        except AttributeError as ae:
            logger.error("[SERVER] Attribute error: %s", ae)
            return remote_pb2.CommandResponse(
                success=False,
                message="Method not found",
                error=str(ae),
                items=[]
            )

        except Exception as e:
            logger.error("[SERVER] Error executing: %s", e)
            return remote_pb2.CommandResponse(
                success=False,
                message="Execution failed",
                error=str(e),
                items=[]
            )

