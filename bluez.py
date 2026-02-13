import dbus
import dbus.mainloop.glib
import dbus.service
import os
import subprocess
import time

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

from libraries.bluetooth import constants
from libraries.bluetooth.agent import AutoAcceptAgent
from Utils.utils import run
from libraries.bluetooth.bt_ble_advertisment import Advertisement

class BluetoothDeviceManager:
    """A class for managing Bluetooth devices using the BlueZ D-Bus API."""

    def __init__(self, log=None, interface=None):
        """Initialize the BluetoothDeviceManager by setting up the system bus and adapter.

        Args:
            log: Logger instance.
            interface: Bluetooth adapter interface (e.g., hci0).
        """
        DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        self.interface = interface
        self.log = log
        self.adapter_path = f'{constants.bluez_path}/{self.interface}'
        self.adapter_proxy = self.bus.get_object(constants.bluez_service, self.adapter_path)
        self.adapter_properties = dbus.Interface(self.adapter_proxy, constants.properties_interface)
        self.adapter = dbus.Interface(self.adapter_proxy, constants.adapter_interface)
        self.object_manager = dbus.Interface(self.bus.get_object(constants.bluez_service, "/"), constants.object_manager_interface)
        self.mainloop = GLib.MainLoop()
        self.agent = None
        self.ad = Advertisement(self.bus, log=self.log)
        self.last_session_path = None
        self.opp_process = None
        self.stream_process = None
        self.on_call_event = None
        self.pulseaudio_process = None
        self.stream_process = None
        self.voice_call_manager = None
        self.device_address = None
        self.device_profiles = {}
        self.device_states = {}

    def power_on_adapter(self):
        """Power on the local Bluetooth adapter using the D-Bus Properties interface."""
        try:
            self.adapter_properties.Set(constants.adapter_interface, "Powered", dbus.Boolean(True))
            if self.log:
                self.log.info(f"Powered on adapter {self.interface}")
        except dbus.DBusException as error:
            if self.log:
                self.log.error(f"Failed to power on adapter {self.interface}: {error}")

    def get_paired_devices(self):
        """Retrieves all Bluetooth devices that are currently paired with the adapter.

        Returns:
            paired_devices: A dictionary of paired devices.
        """
        paired_devices = {}
        for path, interfaces in self.object_manager.GetManagedObjects().items():
            if constants.device_interface in interfaces:
                device = interfaces[constants.device_interface]
                if device.get("Paired") and device.get("Adapter") == self.adapter_path:
                    address = device.get("Address")
                    name = device.get("Name", "Unknown")
                    paired_devices[address] = name
        return paired_devices

    def set_discovery_filter(self, filter_dict):
        """Set the Bluetooth discovery filter via BlueZ.

        Args:
            filter_dict (str): "LE", "BR/EDR", or "ALL"
        """
        try:
            self.adapter.SetDiscoveryFilter(filter_dict)
            self.log.debug("BlueZ discovery filter set: %s", filter_dict)
        except Exception as e:
            self.log.error("Failed to set discovery filter: %s", e)

    def start_discovery(self):
        """Start scanning for nearby Bluetooth devices, if not already discovering."""
        try:
            if not self.adapter_properties.Get(constants.adapter_interface, "Discovering"):
                self.adapter.SetDiscoveryFilter({
                    "Transport": dbus.String("bredr")
                })
                self.adapter.StartDiscovery()
                self.log.info("Discovery started.")
                return True
            else:
                self.log.info("Discovery already in progress.")
        except dbus.exceptions.DBusException as error:
            self.log.error("Failed to start discovery: %s", error)

    def stop_discovery(self):
        """Stop Bluetooth device discovery, if it's started."""
        try:
            if self.adapter_properties.Get(constants.adapter_interface, "Discovering"):
                self.adapter.StopDiscovery()
                self.log.info("Discovery stopped.")
            else:
                self.log.info("Discovery was not started.")
        except dbus.exceptions.DBusException as error:
            self.log.error("Failed to stop discovery: %s", error)

    '''def get_discovered_devices(self):
        """Retrieve discovered Bluetooth devices under the current adapter.

        Returns:
            discovered_devices: List of discovered Bluetooth devices.
        """
        discovered_devices = []
        for path, interfaces in self.object_manager.GetManagedObjects().items():
            device = interfaces.get(constants.device_interface)
            if not device or device.get("Adapter") != self.adapter_path:
                continue
            address = device.get("Address")
            alias = device.get("Alias", "Unknown")
            if address:
                discovered_devices.append({
                    "path": path,
                    "address": address,
                    "alias": alias})
            else:
                self.log.warning("Failed to extract device info from %s", path)
        return discovered_devices'''

    def get_discovered_devices(self):
        try:
            devices = []
            objects = self.object_manager.GetManagedObjects()

            for path, interfaces in objects.items():
                dev = interfaces.get(constants.device_interface)
                if not dev:
                    continue

                devices.append({
                    "address": str(dev.get("Address", "")),
                    "name": str(dev.get("Name", "")),
                })

            return devices

        except Exception as e:
            self.log.error("get_discovered_devices error: %s", e)
            return []  # 🔥 ALWAYS return list

    def get_device_path(self, device_address):
        """Constructs the D-Bus Object path for a bluetooth device using its address.

        Args:
            device_address: Bluetooth address of the remote device.

        Returns:
            device_path: D-Bus Object path.
        """
        formatted_address = device_address.replace(":", "_")
        device_path = f"{constants.bluez_path}/{self.interface}/dev_{formatted_address}"
        return device_path

    def register_agent(self, capability=None, ui_callback=None):
        """Register the Bluetooth agent with Bluez to handle pairing requests.

        Args:
            capability: The I/O capability such as "NoInputNoOutput", "DisplayOnly", etc.
            ui_callback: Callback for UI interactions related to Bluetooth events.

        Returns:
            True if registration succeeds, False otherwise.
        """
        try:
            if self.agent is None:
                self.setup_agent(ui_callback)
            agent_manager = dbus.Interface(self.bus.get_object(constants.bluez_service, constants.bluez_path), constants.agent_interface)
            agent_manager.RegisterAgent(constants.agent_path, capability)
            agent_manager.RequestDefaultAgent(constants.agent_path)
            self.log.info("Registered Agent successfully at %s with capability: %s", constants.agent_path, capability)
            return True
        except dbus.exceptions.DBusException as error:
            self.log.error("Failed to register agent: %s", error)
            return False

    def pair(self, address):
        """Pairs with a Bluetooth device using the given controller interface.

        Args:
            address : Bluetooth address of remote device.

        Returns:
            True if successfully paired, False otherwise.
        """
        device_path = self.get_device_path(address)
        try:
            device_proxy = self.bus.get_object(constants.bluez_service, device_path)
            device = dbus.Interface(device_proxy, constants.device_interface)
            properties = dbus.Interface(device_proxy, constants.properties_interface)
            paired = properties.Get(constants.device_interface, "Paired")
            if paired:
                self.log.info("Device %s is already paired.", address)
                return True
            self.log.info("Initiating pairing with %s", address)
            try:
                device.Pair()

            except dbus.exceptions.DBusException as error:
                if "NoReply" in str(error):
                    self.log.warning("NoReply error during Pair() – continuing to poll for paired state.")
                else:
                    self.log.error("Pairing failed with %s: %s", address, error)
                    return False
            for i in range(10):
                time.sleep(1)
                paired = properties.Get(constants.device_interface, "Paired")
                if paired:
                    return True
            self.log.warning("Pairing not confirmed with %s after timeout.", address)
            return False
        except dbus.exceptions.DBusException as error:
            self.log.error("Pairing failed with %s: %s", address, error)
            return False

    def connect(self, address):
        """Establish a  connection to the specified Bluetooth device.

        Args:
            address: Bluetooth address of remote device.

        Returns:
            True if connected, False otherwise.
        """
        self.device_address = address
        device_path = self.get_device_path(address)
        try:
            device = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.device_interface)
            device.Connect()
            properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.properties_interface)
            connected = properties.Get(constants.device_interface, "Connected")
            if connected:
                self.log.info("Connection successful to %s", address)
                return True
        except Exception as error:
            self.log.info("Connection failed:%s", error)
            return False

    def disconnect(self, address):
        """Disconnect a Bluetooth  device from the specified adapter.

        Args:
            address: Bluetooth address of the remote device.

        Returns:
            True if disconnected or already disconnected, False if an error occurred.
        """
        device_path = self.get_device_path(address)
        try:
            device = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.device_interface)
            properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.properties_interface)
            connected = properties.Get(constants.device_interface, "Connected")
            if not connected:
                self.log.info("Device %s is already disconnected.", address)
                return True
            device.Disconnect()
            return True
        except dbus.exceptions.DBusException as error:
            self.log.info("Error disconnecting device %s:%s", address, error)
            return False

    def unpair_device(self, address):
        """Unpairs a paired or known Bluetooth device from the system using BlueZ D-Bus.

        Args:
            address: The Bluetooth address of the remote device.

        Returns:
            True if the device was unpaired successfully or already not present,
            False if the unpairing failed or the device still exists afterward.
        """
        try:
            target_path = None
            for path, interfaces in self.object_manager.GetManagedObjects().items():
                if constants.device_interface in interfaces and interfaces[constants.device_interface].get("Address") == address and path.startswith(self.adapter_path):
                    target_path = path
                    break
            if not target_path:
                self.log.info("Device with address %s not found on %s", address, self.interface)
                return True
            self.adapter.RemoveDevice(target_path)
            self.log.info("Requested unpair of device %s at path %s", address, target_path)
            time.sleep(0.5)
            for path, interfaces in self.object_manager.GetManagedObjects().items():
                if constants.device_interface in interfaces and interfaces[constants.device_interface].get("Address") == address:
                    self.log.warning("Device %s still exists after attempted unpair", address)
                    return False
            self.log.info("Device %s unpaired successfully", address)
            return True
        except dbus.exceptions.DBusException as error:
            self.log.error("DBusException while unpairing device %s: %s", address, error)
            return False

    def is_device_paired(self, device_address):
        """Checks if the specified device is paired.

        Args:
            device_address: Bluetooth address of remote device.

        Returns:
            True if paired, False otherwise.
        """
        device_path = self.get_device_path(device_address)
        properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.properties_interface)
        try:
            return properties.Get(constants.device_interface, "Paired")
        except dbus.exceptions.DBusException as error:
            self.log.debug("DBusException while checking pairing:%s", error)
            return False

    def is_device_connected(self, device_address):
        """Checks if the specified device is connected.

        Args:
            device_address: Bluetooth address of remote device.

        Returns:
            True if connected, False otherwise.
        """
        device_path = self.get_device_path(device_address)
        try:
            properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.properties_interface)
            connected = properties.Get(constants.device_interface, "Connected")
            if self.interface not in device_path:
                self.log.debug("Device path %s does not match interface %s", device_path, self.interface)
                return False
            return connected
        except dbus.exceptions.DBusException as error:
            self.log.debug("DBusException while checking connection:%s", error)
            return False

    def start_a2dp_stream(self, address, filepath=None):
        """Initiates an A2DP audio stream to a Bluetooth device using PulseAudio.

        Args:
            address: Bluetooth address of the target device.
            filepath: Path to the audio file.

        Returns:
            True if the stream was started, False otherwise.
        """
        device_path = self.get_device_path(address)
        self.log.info("Device path:%s", device_path)
        try:
            self.log.info("Starting A2DP stream to device path: %s with file: %s", device_path, filepath)
            self.stream_process = run(self.log, ["paplay", filepath], block=False)
            return True
        except Exception as error:
            self.log.error("Stream error:%s", error)
            return False

    def stop_a2dp_stream(self):
        """Stop the current A2DP audio stream."""
        if hasattr(self, 'stream_process') and self.stream_process:
            if self.stream_process.poll() is None:
                self.stream_process.terminate()
                self.stream_process.wait()
                self.log.info("Stream terminated successfully.")
            else:
                self.log.info("Stream was already stopped.")
            self.stream_process = None
            return True
        self.log.info("No active stream to stop.")
        return False

    def media_control(self, command, address=None):
        """Sends AVRCP (Audio/Video Remote Control Profile) media control commands to a connected Bluetooth device.

        Args:
            command: The AVRCP command to send. Must be one of: "play", "pause", "next", "previous", "rewind".
            address: Bluetooth address of the target device.
        """
        valid_commands = {"play": "Play",
                 "pause": "Pause",
                 "next": "Next",
                 "previous": "Previous",
                 "rewind": "Rewind"
                          }
        if command not in valid_commands:
            self.log.info("Invalid media control command:%s", command)
        media_control_interface = self.get_media_control_interface(address)
        if not media_control_interface:
            self.log.info(" MediaControl1 interface NOT FOUND")
            return
        self.log.info(" MediaControl1 interface FOUND")
        try:
            getattr(media_control_interface, valid_commands[command])()
            self.log.info("AVRCP %s sent successfully to %s", command, address)
        except Exception as error:
            self.log.warning("AVRCP command %s failed with exception:%s", command, error)

    def get_media_control_interface(self, address):
        """Retrieve the `org.bluez.MediaControl1` D-Bus interface for a given Bluetooth device.

        Args:
            address: The Bluetooth address of the target Bluetooth device.

        Returns:
            The MediaControl1 D-Bus interface if found, otherwise None.
        """
        try:
            formatted_addr = address.replace(":", "_").upper()
            for path, interfaces in self.object_manager.GetManagedObjects().items():
                if constants.media_control_interface in interfaces:
                    if formatted_addr in path and path.startswith(self.adapter_path):
                        self.log.info("Found MediaControl1 at %s", path)
                        return dbus.Interface(self.bus.get_object(constants.bluez_service, path), constants.media_control_interface)
            self.log.info(" No MediaControl1 interface found for %s under %s", address, self.adapter_path)
        except Exception as error:
            self.log.info(" Exception while getting MediaControl1 interface:%s", error)

    def get_a2dp_role_for_device(self, device_address):
        """Get the A2DP role (sink or source) for a specific connected Bluetooth device.

        Args:
            device_address: Bluetooth address of the connected device.

        Returns:
            sink or source
        """
        uuid_map = {"source": "110a", "sink": "110b"}
        for path, interfaces in self.object_manager.GetManagedObjects().items():
            if constants.device_interface in interfaces:
                properties = interfaces[constants.device_interface]
                if properties.get("Address") == device_address and properties.get("Connected") and properties.get("Adapter") == self.adapter_path:
                    uuids = properties.get("UUIDs", [])
                    for role, uuid_role in uuid_map.items():
                        if any(uuid_role in uuid.lower() for uuid in uuids):
                            return role
                        else:
                            self.log.warning("Unknown A2DP role %s", device_address)

    def send_file(self, device_address, file_path, session_path=None, profile=None):
        """Send a file via OBEX OPP and wait for real-time transfer status.

        Args:
            device_address: Bluetooth address of the target device.
            file_path: path of the file to be sent.
            session_path: Existing OBEX session path. If None, a new session is created.
            profile: Name of the profile which will be used to send file.

        Returns:
            Transfer status ("complete", "error", etc.).
        """
        if not os.path.exists(file_path):
            self.log.info("File does not exist: %s", file_path)
            return "error"
        try:
            if not session_path:
                session_path = self.create_obex_session(device_address, profile="opp")
            opp_interface = dbus.Interface(self.session_bus.get_object(constants.obex_service, session_path), constants.obex_object_push)
            transfer_path, _ = opp_interface.SendFile(file_path)
            self.log.info("Started transfer: %s", transfer_path)
            self.transfer_status = {"status": "unknown"}
            self.session_bus.add_signal_receiver(
                self.obex_properties_changed,
                dbus_interface=constants.properties_interface,
                signal_name="PropertiesChanged",
                arg0=constants.obex_object_transfer,
                path=transfer_path,
                path_keyword="path")
            self.transfer_loop = GLib.MainLoop()
            self.transfer_loop.run()
            status = self.transfer_status["status"]
            self.remove_obex_session(session_path)
            return status
        except Exception as error:
            self.log.info("OBEX send failed: %s", error)
            return "error"

    def receive_file(self, save_directory="/tmp", timeout=20, user_confirm_callback=None):
        """Start an OBEX Object Push server and wait for a file to be received.

        Args:
            save_directory: Directory to save the received file. Defaults to "/tmp".
            timeout: Time in seconds to wait for file transfer. Defaults to 20.
            user_confirm_callback: Callback to confirm whether to accept the received file.

        Returns:
            Path to the received file if accepted, otherwise None.
        """
        try:
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            run(self.log, "killall -9 obexpushd")
            self.log.info("Killed existing obexpushd processes..")
            existing_files = set(os.listdir(save_directory))
            self.opp_process = subprocess.Popen(["obexpushd", "-B", "-o", save_directory, "-n"])
            self.log.info("OPP server started. Waiting for incoming file...")
            start_time = time.time()
            while time.time() - start_time < timeout:
                current_files = set(os.listdir(save_directory))
                new_files = current_files - existing_files
                if new_files:
                    received_file = new_files.pop()
                    full_path = os.path.join(save_directory, received_file)
                    self.log.info("Incoming file: %s", received_file)
                    user_accepted = True
                    if user_confirm_callback:
                        user_accepted = user_confirm_callback(full_path)
                    if user_accepted:
                        self.log.info("User accepted file.")
                        self.stop_opp_receiver()
                        return full_path
                    else:
                        self.log.info("User rejected file.")
                        os.remove(full_path)
                        self.stop_opp_receiver()
        except Exception as error:
            self.stop_opp_receiver()
            self.log.error("Error in receive_file:%s", error)

    def stop_opp_receiver(self):
        """Stop the OBEX Object Push server if it's currently running."""
        if self.opp_process and self.opp_process.poll() is None:
            self.opp_process.terminate()
            self.opp_process.wait()
            self.log.info("OPP server stopped.")
        else:
            self.log.info("No OPP server running or already stopped.")

    def obex_properties_changed(self, interface, changed, invalidated, path):
        """Handle the PropertiesChanged signal for an OBEX file transfer.

        Args:
            interface: The D-Bus interface name where the property change occurred.
            changed: A dictionary containing the properties that changed and their new values.
            invalidated: A list of properties that are no longer valid.
            path: The D-Bus object path for the signal.
        """
        if "Status" in changed:
            status = str(changed["Status"])
            self.log.info("Signal: Transfer status changed to:%s", status)
            self.transfer_status["status"] = status
            if status in ["complete", "error", "cancelled"]:
                if hasattr(self, "transfer_loop") and self.transfer_loop.is_running():
                    self.transfer_loop.quit()
            else:
                self.log.warning("PropertiesChanged received without 'Status': %s", changed)

    def set_discoverable_mode(self, enable):
        """Enable or disable discoverable mode on the Bluetooth adapter.

        Args:
            enable: True to enable, False to disable.
        """
        if enable:
            command = f"hciconfig {self.interface} piscan"
            subprocess.run(command, shell=True)
            self.log.info("Bluetooth device is now discoverable.")
            return True
        else:
            self.log.info("Setting Bluetooth device to be non-discoverable...")
            command = f"hciconfig {self.interface} noscan"
            subprocess.run(command, shell=True)
            self.log.info("Bluetooth device is now non-discoverable.")
            return True

    def trust_device(self, address):
        """Marks a Bluetooth device as trusted on the system using BlueZ D-Bus.

        Args:
            address: Bluetooth address of the remote device to be trusted.

        Returns:
            True if the device was successfully marked as trusted, False otherwise.
        """
        try:
            device_path = f"/org/bluez/hci0/dev_{address.replace(':', '_')}"
            device = self.bus.get_object("org.bluez", device_path)
            props = dbus.Interface(device, "org.freedesktop.DBus.Properties")
            props.Set("org.bluez.Device1", "Trusted", dbus.Boolean(True))
            self.log.info("[Info] Trusted device: %s", address)
            return True
        except Exception as error:
            self.log.error("[Error] Could not trust device %s: %s", address, error)
            return False

    def create_obex_session(self, device_address, profile):
        """Creates an OBEX Object Push (OPP) session.

        Args:
            device_address: Bluetooth address of remote device.
            profile: Name of the profile to create obex session.

        Returns:
            session_path: The OBEX session path if successful, else return False.
        """
        try:
            self.session_bus = dbus.SessionBus()
            self.obex_manager = dbus.Interface(self.session_bus.get_object(constants.obex_service, constants.obex_path), constants.obex_client)
            session_path = self.obex_manager.CreateSession(device_address, {"Target": dbus.String(profile)})
            self.last_session_path = session_path
            self.log.info("Created OBEX OPP session: %s", session_path)
            return session_path
        except Exception as error:
            self.log.error("OBEX session creation failed for device %s: %s", device_address, error)
            return False

    def remove_obex_session(self, session_path):
        """Removes the given OBEX session.

        Args:
            session_path: Existing OBEX session path.
        """
        try:
            self.obex_manager.RemoveSession(session_path)
            self.log.info("Removed OBEX session: %s", session_path)
        except Exception as error:
            self.log.warning("Failed to remove session: %s", error)
        self.last_session_path = None

    def get_media_dbus_path(self, address, interface_name):
        """
        Find the BlueZ D-Bus object path for a given device and interface.

        Args:
            address: Bluetooth MAC address.
            interface_name: The BlueZ interface to match, e.g.,constants.media_player_interface
                            or constants.media_transport_interface.

        Returns:
            The D-Bus object path if found, otherwise None.
        """
        formatted = address.replace(":", "_").upper()
        for path, interfaces in self.object_manager.GetManagedObjects().items():
            if interface_name in interfaces:
                if formatted in path and path.startswith(self.adapter_path):
                    return path
        return None

    def get_media_playback_info(self, address):
        """Retrieve playback status, track info, and position using MediaPlayer1.

        Args:
            address: Bluetooth address of remote device.

        Returns:
            status, track, position (ms), duration (ms), or None if unavailable.
        """
        try:
            path = self.get_media_dbus_path(address, constants.media_player_interface)
            if not path:
                return None

            media_player = dbus.Interface(
                self.bus.get_object(constants.bluez_service, path),
                constants.media_player_interface
            )
            props = dbus.Interface(media_player, constants.properties_interface)

            status = props.Get(constants.media_player_interface, "Status")
            track = props.Get(constants.media_player_interface, "Track")
            position = props.Get(constants.media_player_interface, "Position")
            duration = track.get("Duration", 0)

            return {
                "status": str(status),
                "track": {
                    "title": str(track.get("Title", "")),
                    "artist": str(track.get("Artist", "")),
                    "album": str(track.get("Album", "")),
                },
                "position": int(position),
                "duration": int(duration),
            }
        except Exception as error:
            self.log.warning("Failed to get media playback info: %s", error)
            return None

    def get_media_volume(self, address):
        """Get the current A2DP volume for the given device.

        Args:
            address: Bluetooth address of remote device.

        Returns:
            The volume level as an integer if available, otherwise None.
        """
        try:
            path = self.get_media_dbus_path(address, constants.media_transport_interface)
            if not path:
                return None

            transport = dbus.Interface(
                self.bus.get_object(constants.bluez_service, path),
                constants.properties_interface
            )
            volume = transport.Get(constants.media_transport_interface, "Volume")
            return int(volume)
        except Exception as error:
            self.log.warning("Failed to get volume: %s", error)
            return None

    def set_media_volume(self, address, volume):
        """Set A2DP volume (0–127) for the given device.

        Args:
            address: Bluetooth address of remote device.
            volume: Integer volume level to set.

        Returns:
            True if the volume was set successfully, otherwise False.
        """
        try:
            path = self.get_media_dbus_path(address, constants.media_transport_interface)
            if not path:
                return False

            transport = dbus.Interface(
                self.bus.get_object(constants.bluez_service, path),
                constants.properties_interface
            )
            transport.Set(constants.media_transport_interface, "Volume", dbus.UInt16(volume))
            self.log.info("Volume set to %d", volume)
            return True
        except Exception as error:
            self.log.warning("Failed to set volume: %s", error)
            return False

    def get_connected_profile_uuids(self, device_address):
        """Retrieves the list of UUIDs for the Bluetooth profiles connected to the device
          identified by the given device address.

        Args:
            device_address: Bluetooth address of remote device.

        Returns:
            A list of UUID strings representing the connected profiles.
            Returns an empty list if the UUIDs cannot be retrieved.
        """
        device_path = self.get_device_path(device_address)
        device = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path), constants.device_interface)
        properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path),
                                    constants.properties_interface)
        try:
            uuids = properties.Get(constants.device_interface, 'UUIDs')
            return uuids
        except Exception as error:
            self.log.info(f"Failed to get UUIDs for {device_address}: {error}")
            return []

    def connect_profile(self, address, profile_uuid):
        """
        Connect to a specific Bluetooth profile (e.g., A2DP Sink) on the remote device.

        Args:
            address: Bluetooth address of remote device.
            profile_uuid: UUID of the Bluetooth profile to connect.

        Returns:
            True if the profile was connected, False otherwise.
        """
        device_path = self.get_device_path(address)
        if not device_path:
            self.log.info("Device path not found for address %s", address)
            return False
        try:
            device = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path),
                                    constants.device_interface)
            device.ConnectProfile(profile_uuid)
            self.log.info("Profile %s successfully connected to %s", profile_uuid, address)
            return True
        except Exception as error:
            self.log.error("Failed to connect profile %s: %s", profile_uuid, error)
            return False

    def handle_connect(self, device_address, selected_profiles, load_profiles):
        """Connects a Bluetooth device with the specified profiles and tracks connection results.

        Args:
            device_address : The Bluetooth address of remote device.
            selected_profiles: A dictionary mapping profile names to roles.
            load_profiles: Flag indicating whether to load previously stored profiles (currently unused).

        Returns:
            True if all selected profiles connected successfully, False otherwise.
            or a descriptive message listing connected and failed profiles.
        """
        self.device_profiles[device_address] = []
        failed_profiles = []

        for profile, role in selected_profiles.items():
            result = self.profile_connection(device_address, profile, role)
            failed_profiles.extend(result)

        if not failed_profiles:
            success = True
            message = f"Connected profiles: {', '.join(self.device_profiles[device_address])}"
        else:
            success = False
            message_parts = []
            if self.device_profiles[device_address]:
                message_parts.append(f"Successfully connected: {', '.join(self.device_profiles[device_address])}")
            message_parts.append("Failed to connect:")
            message_parts.extend(f" - {p}" for p in failed_profiles)
            message = "\n".join(message_parts)

        return success, message

    def profile_connection(self, device_address, profile, role=None):
        """Attempts to connect a specific Bluetooth profile for a device.

        Args:
            device_address: The Bluetooth address of the device.
            profile: The profile to connect ('all', 'a2dp', 'opp', 'hfp').
            role : Role for A2DP profile ('sink' or 'source'). Defaults to None.

        Returns:
            A list of profile names that failed to connect. Empty list if successful.
        """
        self.device_profiles.setdefault(device_address, [])
        self.device_states.setdefault(device_address, {})

        if profile == 'all':
            # TODO: Better handle connecting multiple profiles at once
            failed = []

            if not self.connect(device_address):
                return ["A2DP", "OPP", "HFP", "PBAP"]

            connected_uuids = self.get_connected_profile_uuids(device_address)
            if constants.profile_uuids["A2DP Sink"] in connected_uuids or constants.profile_uuids["A2DP Source"] in connected_uuids:
                self.device_profiles[device_address].append("A2DP")
            else:
                failed.append("A2DP")

            if constants.profile_uuids["OPP"] in connected_uuids:
                opp_session = self.create_obex_session(device_address, "opp")
                if opp_session:
                    self.device_profiles[device_address].append("OPP")
                    self.device_states[device_address]["session_path"] = opp_session
                else:
                    failed.append("OPP")
            else:
                failed.append("OPP")

            if constants.profile_uuids.get("PBAP") in connected_uuids:
                pbap_session = self.create_obex_session(device_address, "pbap")
                if pbap_session:
                    self.select_phonebook(constants.location["internal"], constants.phonebook_types["phonebook"], pbap_session)
                    self.device_states[device_address]["pbap_session"] = pbap_session
                    self.device_profiles[device_address].append("PBAP")
                else:
                    failed.append("PBAP")
            else:
                failed.append("PBAP")
            if constants.profile_uuids["HFP AG"] in connected_uuids:
                self.device_profiles[device_address].append("HFP")
            else:
                failed.append("HFP")

            return failed

        elif profile == 'a2dp':
            uuid = constants.profile_uuids["A2DP Sink"] if role == 'sink' else constants.profile_uuids["A2DP Source"]
            if self.connect_profile(device_address, profile_uuid=uuid):
                self.device_profiles[device_address].append("A2DP")
                return []
            return ["A2DP"]

        elif profile == 'opp':
            session_path = self.create_obex_session(device_address, "opp")
            if session_path:
                self.device_profiles[device_address].append("OPP")
                self.device_states[device_address]["session_path"] = session_path
                return []
            return ["OPP"]

        elif profile == 'pbap':
            session_path = self.create_obex_session(device_address, "pbap")
            if session_path:
                self.select_phonebook(constants.location["internal"], constants.phonebook_types["phonebook"], session_path)
                self.device_profiles[device_address].append("PBAP")
                self.device_states[device_address]["pbap_session"] = session_path
                return []
            return ["PBAP"]

        elif profile == 'hfp':
            uuid = constants.profile_uuids["HFP AG"]
            if self.connect_profile(device_address, profile_uuid=uuid):
                self.device_profiles[device_address].append("HFP")
                return []
            return ["HFP"]

    def handle_disconnect(self, device_address):
        """Disconnects a Bluetooth device and cleans up its associated sessions and state.

        Args:
            device_address: Bluetooth address of remote device.
        """
        state = self.device_states.get(device_address, {})
        session_path = state.get("session_path")
        pbap_session = state.get("pbap_session")
        opp_connected = "OPP" in self.device_profiles.get(device_address, [])
        a2dp_connected = "A2DP" in self.device_profiles.get(device_address, [])
        hfp_connected = "HFP" in self.device_profiles.get(device_address, [])
        pbap_connected = "PBAP" in self.device_profiles.get(device_address, [])
        bluetooth_connected = self.is_device_connected(device_address)
        bt_success = True

        if opp_connected and session_path:
            self.remove_obex_session(session_path)
            state["session_path"] = None
            self.device_states[device_address] = state

        if a2dp_connected or bluetooth_connected:
            bt_success = self.disconnect(device_address)

        if hfp_connected or bluetooth_connected:
            bt_success = self.disconnect(device_address)

        if pbap_connected and pbap_session:
            self.remove_obex_session(pbap_session)
            state["pbap_session"] = None
            self.device_states[device_address] = state

        # Clean up device state
        self.device_profiles.pop(device_address, None)
        self.device_states.pop(device_address, None)

        return bt_success

    def select_phonebook(self, location, phonebook_type, session_path=None):
        """ Select the phonebook object  to interact with.
        Args:
            location: Phonebook storage location (e.g., "int"(internal which is default), "sim1" and "sim2")
            phonebook_type: Phonebook type (e.g., "pb", "ich", "och", "mch", "cch", "spd", "fav")
            session_path: OBEX session path. Defaults to None.

        Returns:
            True if phonebook was selected successfully, False otherwise. """
        pbap_interface = dbus.Interface(
            self.session_bus.get_object(constants.obex_service, session_path),
            constants.obex_pbap_interface
        )
        if not pbap_interface:
            self.log.error(" Phonebook interface not initialized.")
            return False
        try:
            pbap_interface.Select(location, phonebook_type)
            self.log.debug(f"Selected {location}/{phonebook_type} phonebook.")
            return True
        except dbus.exceptions.DBusException:
            return False

    def pull_single_contact(self, device_address, contact_name, session_path=None, save_path=None):
        """Pull a single contact from a remote device via PBAP.

        Args:
            device_address: Bluetooth address of the remote device.
            contact_name: Name of the contact to pull.
            session_path: Existing OBEX session path. If None, a new session is created. Defaults to None.
            save_path: Local path to save the vCard. Defaults to None.

        Returns:
            Status of the transfer ('complete', 'error', or other status reported by OBEX).
        """
        try:
            if not session_path:
                session_path = self.create_obex_session(device_address, profile="pbap")

            pbap_interface = dbus.Interface(
                self.session_bus.get_object(constants.obex_service, session_path),
                constants.obex_pbap_interface
            )

            transfer_path, _ = pbap_interface.Pull(contact_name, save_path, {})

            self.transfer_status = {"status": "unknown"}
            self.session_bus.add_signal_receiver(
                self.obex_properties_changed,
                dbus_interface=constants.properties_interface,
                signal_name="PropertiesChanged",
                arg0=constants.obex_object_transfer,
                path=transfer_path,
                path_keyword="path"
            )

            self.transfer_loop = GLib.MainLoop()
            self.transfer_loop.run()

            return self.transfer_status["status"]
        except Exception as e:
            self.log.info("PBAP single contact pull failed: %s", e)
            return "error"

    def pull_all_contacts(self, device_address, save_path, session_path):
        """Pull all contacts from a remote device via PBAP.

        Args:
            device_address: Bluetooth address of the remote device.
            save_path: Local directory or file path to save the vCards.
            session_path: Existing OBEX session path. If None, a new session is created. Defaults to None.

        Returns:
            Status of the transfer ('complete', 'error', or other status reported by OBEX).
        """
        try:
            if not session_path:
                session_path = self.create_obex_session(device_address, profile="pbap")

            pbap_interface = dbus.Interface(
                self.session_bus.get_object(constants.obex_service, session_path),
                constants.obex_pbap_interface
            )

            transfer_path, _ = pbap_interface.PullAll(save_path, {})

            self.transfer_status = {"status": "unknown"}
            self.session_bus.add_signal_receiver(
                self.obex_properties_changed,
                dbus_interface=constants.properties_interface,
                signal_name="PropertiesChanged",
                arg0=constants.obex_object_transfer,
                path=transfer_path,
                path_keyword="path"
            )

            self.transfer_loop = GLib.MainLoop()
            self.transfer_loop.run()

            return self.transfer_status["status"]
        except Exception as e:
            self.log.info("PBAP pull all contacts failed: %s", e)
            return "error"

    def setup_agent(self, ui_callback=None):
        """Ensures the Bluetooth agent object is created and ready.

        Args:
            ui_callback: Callback function to handle user interactions.
        """
        self.agent = AutoAcceptAgent(self.bus)

    def unregister_agent(self):
        """Unregister the Bluetooth agent from Bluez."""
        try:
            agent_manager = dbus.Interface(self.bus.get_object(constants.bluez_service, constants.bluez_path),
                                           constants.agent_interface)
            agent_manager.UnregisterAgent(constants.agent_path)
            self.log.info("Unregistered agent from BlueZ.")
        except dbus.exceptions.DBusException as error:
            self.log.error("Failed to unregister agent: %s", error)

    def setup_pairing_signal_listener(self, status_update_handler):
        """Setup D-Bus signal listener for pairing status changes.

        Args:
            status_update_handler: Function to handle pairing status updates.
        """
        self.pairing_status_callback = status_update_handler
        self.bus.add_signal_receiver(
            self.on_pairing_properties_changed,
            dbus_interface="org.freedesktop.DBus.Properties",
            signal_name="PropertiesChanged",
            arg0="org.bluez.Device1",
            path_keyword="path")

    def on_pairing_properties_changed(self, interface, changed, invalidated, path):
        """Listens to changes in "Paired" property in "org.bluez.Device1" interface.

        Args:
            interface: The D-Bus interface name where the property change occurred.
            changed: A dictionary containing the properties that changed and their new values.
            invalidated: A list of properties that are no longer valid.
            path: The D-Bus object path for the signal.
        """
        if interface != "org.bluez.Device1" or "Paired" not in changed:
            return
        paired = changed["Paired"]
        device_address = path.split("dev_")[-1].replace("_", ":")
        if hasattr(self, "pairing_status_callback"):
            self.pairing_status_callback(device_address, paired)

    def get_ofono_modem_path(self, device_address):
        """Gets the ofono modem path.

        Args:
            device_address: Bluetooth address of remote device.
        """
        try:
            manager = dbus.Interface(self.bus.get_object(constants.ofono_bus, "/"), constants.ofono_manager)
            formatted_addr = device_address.replace(":", "_").upper()
            for path, properties in manager.GetModems():
                if formatted_addr in str(path):
                    return path
        except Exception as error:
            self.log.error("Failed to get oFono modem path: %s", error)

    def answer_call(self, device_address):
        """Answer an incoming call on the device.

        Args:
            device_address: Bluetooth address of remote device.
        """
        try:
            call_interface = dbus.Interface(self.bus.get_object("org.ofono", self.active_call_path),
                                            "org.ofono.VoiceCall")
            call_interface.Answer()
            return True
        except Exception as error:
            self.log.error("Failed to answer call on %s: %s", device_address, error)
            return False

    def hangup_all_calls(self, device_address):
        """Hangs up all the active calls.

        Args:
            device_address: Bluetooth address of remote device.
        """
        try:
            self.voice_call_manager.HangupAll()
            return True
        except Exception as error:
            self.log.error("Failed to hangup call on %s: %s", device_address, error)
            return False

    def dial_number(self, device_address, number, hide_callerid="default"):
        """Dial a specific phone number.

        Args:
            device_address: Bluetooth address of remote device.
            number: Number typed by user.
            hide_callerid: whether to hide caller id or not.
        """
        try:
            call_path = self.voice_call_manager.Dial(number, hide_callerid)
            self.log.info("Dialed number %s on %s, call path: %s", number, device_address, call_path)
            return call_path
        except Exception as error:
            self.log.error("Failed to dial on %s: %s", device_address, error)
            return False

    def dial_last(self, device_address):
        """Initiates a new outgoing call to the last dialled number.

        Args:
            device_address: Bluetooth address of remote device.
        """
        try:
            call_path = self.voice_call_manager.DialLast()
            self.log.info("Dialed number, call path: %s", call_path)
            return call_path
        except Exception as error:
            self.log.error("Failed to dial on %s: %s", device_address, error)
            return False

    def hangup_active_call(self):
        """Hang up the current active call."""
        if not self.active_call_path:
            self.log.warning("No active call to hang up.")
            return
        try:
            call_interface = dbus.Interface(self.bus.get_object("org.ofono", self.active_call_path),
                                            "org.ofono.VoiceCall")
            call_interface.Hangup()
            self.log.info(f"Hung up call: {self.active_call_path}")
        except Exception as error:
            self.log.error(f"Failed to hang up: {error}")

    def on_call_added(self, call_path, properties):
        """Triggered when a new call starts or incoming call detected."""
        self.active_call_path = call_path
        number = properties.get("LineIdentification", "Unknown")
        state = properties.get("State", "unknown")
        incoming = properties.get("Incoming", None)

        self.active_calls[call_path] = number

        call_interface = dbus.Interface(self.bus.get_object("org.ofono", call_path), "org.freedesktop.DBus.Properties")
        call_interface.connect_to_signal("PropertiesChanged",
                                         lambda interface, changed, invalid: self.on_call_state_changed(call_path,
                                                                                                        changed))

        if incoming is True or state.lower() == "incoming":
            call_type = "incoming"
        else:
            call_type = "dialing"
        self.notify_call_event(call_path, number, call_type)

    def on_call_removed(self, call_path):
        """Triggered when a call ends."""
        if call_path in self.active_calls:
            del self.active_calls[call_path]

    def get_active_calls(self):
        """Returns dictionary of current active calls {call_path: caller_number}."""
        return self.active_calls

    def setup_hfp_manager(self, device_address):
        """Initialize oFono VoiceCallManager and connect to call signals.

        Args:
            device_address: Bluetooth address of remote device.
        """
        path = self.get_ofono_modem_path(device_address)
        if not path:
            self.log.warning(f"No ofono path for {device_address}")
            return
        try:
            self.active_calls = {}
            self.voice_call_manager = dbus.Interface(self.bus.get_object("org.ofono", path),
                                                     "org.ofono.VoiceCallManager")
            self.voice_call_manager.connect_to_signal("CallAdded", self.on_call_added)
            self.voice_call_manager.connect_to_signal("CallRemoved", self.on_call_removed)

            self.log.info("VoiceCallManager initialized for %s", device_address)
        except Exception as error:
            self.log.error("Failed to setup VoiceCallManager for %s: %s", device_address, error)

    def create_multiparty(self, device_address):
        """Creates a multiparty call.

        Args:
            device_address: Bluetooth address of remote device.

        Returns:
            The list of calls in the multiparty or empty list.
        """
        try:
            multiparty_calls = self.voice_call_manager.CreateMultiparty()
            self.log.info("Multiparty call created on %s, calls:%s", device_address, multiparty_calls)
            return multiparty_calls
        except Exception as error:
            self.log.error("Failed to create multiparty call on %s: %s", device_address, error)
            return []

    def hangup_multiparty(self, device_address):
        """Hangs up the existing multiparty call

        Args:
            device_address: Bluetooth address of remote device.
        """
        try:
            self.voice_call_manager.HangupMultiparty()
            self.log.info("Hangup multiparty on %s, device_address")
            return True
        except Exception as error:
            self.log.error("Failed to hangup multiparty call on %s: %s", device_address, error)
            return False

    def private_chat(self, device_address, call_path):
        """Switch audio to private chat for the selected call.

        Args:
            device_address: Bluetooth address of remote device.
            call_path: Call path of the existing call.

        Returns:
             True if the operation succeeded, False if an exception occurred.
        """
        try:
            self.voice_call_manager.PrivateChat(call_path)
            self.log.info(f"Activated Private Chat for call: {call_path}")
            return True
        except Exception as error:
            self.log.error(f"Failed to activate private chat for {device_address}: {error}")
            return False

    def hold_and_answer(self, device_address):
        """Puts the currently active call on hold and answers a waiting call.

         Args:
             device_address: The Bluetooth address of the remote device.

         Returns:
             True if the operation succeeded, False if an exception occurred.
         """
        try:
            self.voice_call_manager.HoldAndAnswer()
            self.log.info("Active call put on hold and answered waiting call on %s, device_address")
            return True
        except Exception as error:
            self.log.error("Failed to  hold and answer  call on %s: %s", device_address, error)
            return False

    def release_and_swap(self, device_address):
        """Releases the active call and answers a waiting call.

        Args:
            device_address: The Bluetooth address of the device where the call is active.

        Returns:
            True if the operation succeeded, False if an exception occurred.
        """
        try:
            self.voice_call_manager.ReleaseAndSwap()
            self.log.info("Released active calls and answered the waiting call on %s, device_address")
            return True
        except Exception as error:
            self.log.error("Failed to release and answer call on %s: %s", device_address, error)
            return False

    def swap_calls(self, device_address):
        """Swaps the active call with a held or waiting call.

        Args:
            device_address: The Bluetooth address of the remote device.

        Returns:
            True if the operation succeeded, False if an exception occurred.
        """
        try:
            self.voice_call_manager.SwapCalls()
            self.log.info("Swapped active and waiting calls on %s, device_address")
            return True
        except Exception as error:
            self.log.error("Failed to release and answer call on %s: %s", device_address, error)
            return False

    def transfer_calls(self, device_address):
        """Transfers calls between devices (e.g., from hands-free to handset).

        Args:
            device_address : The Bluetooth address of the remote device.

        Returns:
            True if the operation succeeded, False if an exception occurred.
        """
        try:
            self.voice_call_manager.Transfer()
            self.log.info("Transferred calls on %s", device_address)
            return True
        except Exception as error:
            self.log.error("Failed to release and answer call on %s: %s", device_address, error)
            return False

    def send_dtmf_tones(self, device_address, tones):
        """Sends DTMF (Dual-Tone Multi-Frequency) tones during an active call.

         Args:
             device_address: The Bluetooth address of the remote device.
             tones: A string of DTMF tones to send (e.g., '123#').

         Returns:
             True if the tones were sent successfully, False if an exception occurred.
         """
        try:
            self.voice_call_manager.SendTones(tones)
            self.log.info("Send DTMF tones %s to device %s", tones, device_address)
            return True
        except Exception as error:
            self.log.error("Failed to send DTMF tones to %s: %s", device_address, error)
            return False

    def notify_call_event(self, call_path, number, state):
        """Notifies registered listeners of a call state event.

        Args:
            call_path: The D-Bus path of the call.
            number: The phone number associated with the call.
            state: The current state of the call (e.g., 'active', 'held', 'incoming').
        """
        if callable(self.on_call_event):
            self.on_call_event(call_path, number, state)

    def on_call_state_changed(self, call_path, changed):
        """Handles call state changes received from the Bluetooth stack and triggers notifications.

        Args:
            call_path: The D-Bus path of the call.
            changed: Dictionary containing changed properties, including 'State'.
        """
        if "State" in changed:
            state = changed["State"]
            number = self.active_calls.get(call_path, "Unknown")
            state_map = {"active": "active",
                         "held": "held",
                         "disconnected": "disconnected",
                         "incoming": "incoming",
                         "dialing": "dialing",
                         "alerting": "ringing"}
            mapped_state = state_map.get(state.lower(), state)
            self.notify_call_event(call_path, number, mapped_state)

    def get_connected_devices(self):
        """Returns connected devices on this adapter.

        Returns:
            connected: Mapping of device addresses to device names.
        """
        try:
            connected = {}
            for path, interfaces in self.object_manager.GetManagedObjects().items():
                device = interfaces.get(constants.device_interface)
                if not device:
                    continue
                if device.get("Connected") and device.get("Adapter") == self.adapter_path:
                    connected[device.get("Address")] = device.get("Name", "Unknown")
            return connected
        except Exception as error:
            self.log.error(f"get_connected_devices: {error}")
            return {}

    def start_le_discovery(self):
        """Start le scanning for nearby Bluetooth devices, if not already discovering."""
        try:
            if not self.adapter_properties.Get(constants.adapter_interface, "Discovering"):
                self.log.info("Starting LE discovery")
                self.adapter.SetDiscoveryFilter({
                "Transport": dbus.String("le")
                })
                self.adapter.StartDiscovery()
                self.log.info("Discovery started.")
                return True
        except Exception as error:
            self.log.error("Failed to start discovery: %s", error)
            return False

    def le_scan_connect(self, address):
        """Scan and connect to a remote le device.

        Args:
            address: Bluetooth address of remote device.
        """
        device_path = self.get_device_path(address)
        self.log.debug("Starting LE scan")
        self.start_le_discovery()
        time.sleep(2)
        self.log.debug("Connecting to device {}".format(address))
        self.device_address = address
        try:
            device = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path),
                                    constants.device_interface)
            device.Connect()
            self.log.debug("Stopping LE scan")
            self.stop_discovery()
            properties = dbus.Interface(self.bus.get_object(constants.bluez_service, device_path),
                                    constants.properties_interface)
            connected = properties.Get(constants.device_interface, "Connected")
            if connected:
                self.log.info("Connection successful to %s", address)
                return True
        except Exception as error:
            self.log.error("le connect failed: %s", error)

    def set_pairable(self, mode):
        """Set adapter pairable mode.

        Args:
            mode: 1 (enable) or 0 (disable)

        Returns:
            True if pairable state matches requested mode
        """
        self.log.debug(f"Setting pairable mode to {mode}")
        self.adapter_properties.Set(
            constants.adapter_interface,
            "Pairable",
            dbus.Boolean(bool(mode))
        )
        if mode:
            self.adapter_properties.Set(
                constants.adapter_interface,
                "PairableTimeout",
                dbus.UInt32(0)
            )
        pairable_mode = bool(self.adapter_properties.Get(constants.adapter_interface, "Pairable"))
        self.log.debug(f"Pairable mode set to: {pairable_mode}")
        return True

    def reset_dut(self):
        """Minimal DUT reset:"""
        self.log.info("unpairing PTS device")
        try:
            self.unpair_device(constants.pts_address)
            self.log.info("PTS device unpaired")
        except Exception as error:
            self.log.warning(f"Failed to unpair PTS device: {error}")

    def wait_for_any_advertisement(self, timeout=15):
        """Listen for advertisement from the specified address

        Args:
            timeout: Timeout in seconds.
        """
        self.log.info("Waiting for PTS advertising...")
        self.start_le_discovery()
        start = time.time()
        while time.time() - start < timeout:
            try:
                for path, interfaces in self.object_manager.GetManagedObjects().items():
                    dev = interfaces.get(constants.device_interface)
                    if not dev:
                        continue
                    addr = dev.get("Address", "")
                    name = dev.get("Name", "")
                    if (addr == constants.pts_address or name.startswith("PTS") or "PTS" in name):
                        self.log.info(f"PTS advertising detected: {addr} {name}")
                        self.stop_discovery()
                        return True
            except Exception as error:
                self.log.debug(f"Discovery error: {error}")
            time.sleep(0.5)
        self.stop_discovery()
        self.log.warning("PTS advertising NOT detected")
        return False

    def build_adv_payload(self, structure_key):
        """Build advertising payload from structured AD fields.

        Args:
            structure_key:Key from constants.advertisement_structures.

        Returns:
            formatted payload for hcitool.
        """
        structure = constants.adv_structures[structure_key]
        total_length = len(structure)
        if total_length > 31:
            raise ValueError("Advertising payload exceeds 31 bytes")
        padded_structure = structure + ["00"] * (31 - total_length)
        payload = f"{total_length:02x} " + " ".join(padded_structure)
        self.log.debug(
            "Built advertising payload (%s): %s",
            structure_key,
            payload,
        )
        return payload

    def start_advertising(self, advertisement_data_key=None, advertisement_structure_key=None, advertisement_param_key="connectable", random_addr_key=None):
        """Start BLE advertising using either predefined payload or structured payload.

        Args:
            advertisement_data_key:
                Example: "pts_general", "pts_limited", "service_uuid"

            advertisement_structure_key:
                Example: "flags", "manufacturer", "tx_power"

            advertisement_param_key:
                Example: "connectable", "non_connectable", "broadcast"

            random_addr_key:
                Example: "nrpa"

        Returns:
            True if advertising started successfully
        """
        if not advertisement_data_key and not advertisement_structure_key:
            raise ValueError(
                "Either advertisement_data_key or advertisement_structure_key must be provided"
            )
        self.log.info(
            "Starting advertising: advertisement_data=%s advertisement_structure=%s params=%s random_addr=%s",
            advertisement_data_key,
            advertisement_structure_key,
            advertisement_param_key,
            random_addr_key,
        )
        run(
            self.log,
            f"hcitool -i {self.interface} cmd "
            f"{constants.cmd['le_set_advertisement_enable']} 00",
        )
        time.sleep(0.2)
        if random_addr_key:
            self.log.info("Setting random address: %s", random_addr_key)
            run(
                self.log,
                f"hcitool -i {self.interface} cmd "
                f"{constants.cmd['le_set_random_addr']} "
                f"{constants.random_address[random_addr_key]}",
            )
        if advertisement_structure_key:
            payload = self.build_adv_payload(advertisement_structure_key)
        else:
            payload = constants.adv_data[advertisement_data_key]
        run(
            self.log,
            f"hcitool -i {self.interface} cmd "
            f"{constants.cmd['le_set_advertisement_data']} "
            f"{payload}",
        )
        run(
            self.log,
            f"hcitool -i {self.interface} cmd "
            f"{constants.cmd['le_set_advertisement_params']} "
            f"{constants.adv_params[advertisement_param_key]}",
        )
        run(self.log,
            f"hcitool -i {self.interface} cmd "
            f"{constants.cmd['le_set_advertisement_enable']} 01",
        )
        self.log.info("Advertising started successfully")
        return True

    def stop_advertising(self):
        """Disable BLE advertising.
        Sends LE Set Advertising Enable command with value 0x00.
        """
        self.log.info("Stopping advertising")
        run(self.log, f"hcitool -i {self.interface} cmd " f"{constants.cmd['le_set_advertisement_enable']} 00")

    def general_discoverable_advertise(self, connectable=False):
        """Start General Discoverable advertising.

        Args:
            connectable:
                True  - ADV_IND (connectable)
                False - ADV_NONCONN_IND (non-connectable)

        Returns:
            True if advertising started successfully
        """
        self.log.info("Enabling General Discoverable advertising")
        adv_param_key = "connectable" if connectable else "non_connectable"
        return self.start_advertising(
            adv_data_key="pts_general",
            adv_param_key=adv_param_key
        )

    def set_connectable(self, enable):
        """Enable or disable BR/EDR connectability (page scan)."""
        try:
            if enable:
                cmd = f"hciconfig {self.interface} pscan"
            else:
                cmd = f"hciconfig {self.interface} noscan"
            run(self.log, cmd)
            self.log.info("BR/EDR connectable set to %s", enable)
            return True
        except Exception as e:
            self.log.error("Failed to set connectable: %s", e)
            return False
