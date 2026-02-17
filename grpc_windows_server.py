2026-02-17 13:35:48,529 | INFO | [INFO] Detecting Bluetooth interfaces...
2026-02-17 13:35:48,669 | INFO | Command: hciconfig -a | grep -B 2 "BD A"
Output: hci0:	Type: Primary  Bus: USB
	BD Address: 5C:F3:70:60:1D:A1  ACL MTU: 1021:8  SCO MTU: 64:1
2026-02-17 13:35:48,670 | INFO | Controllers {'5C:F3:70:60:1D:A1 ': 'hci0'} found on host
2026-02-17 13:35:48,670 | INFO | [INFO] Using interface: hci0
2026-02-17 13:35:48,670 | INFO | [INFO] Initializing BluetoothDeviceManager...
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/dbus/bus.py", line 177, in activate_name_owner
    return self.get_name_owner(bus_name)
  File "/usr/lib/python3/dist-packages/dbus/bus.py", line 361, in get_name_owner
    return self.call_blocking(BUS_DAEMON_NAME, BUS_DAEMON_PATH,
  File "/usr/lib/python3/dist-packages/dbus/connection.py", line 652, in call_blocking
    reply_message = self.send_message_with_reply_and_block(
dbus.exceptions.DBusException: org.freedesktop.DBus.Error.NameHasNoOwner: Could not get owner of name 'org.bluez': no such name

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "server.py", line 34, in <module>
    serve()
  File "server.py", line 23, in serve
    remote_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
  File "/root/pts-grpc/stub_bluetooth.py", line 116, in __init__
    self._init_bt_components()
  File "/root/pts-grpc/stub_bluetooth.py", line 166, in _init_bt_components
    self.bt_manager = BluetoothDeviceManager(log=logger, interface=interface)
  File "/root/pts-grpc/libraries/bluetooth/bluez.py", line 31, in __init__
    self.adapter_proxy = self.bus.get_object(constants.bluez_service, self.adapter_path)
  File "/usr/lib/python3/dist-packages/dbus/bus.py", line 241, in get_object
    return self.ProxyObjectClass(self, bus_name, object_path,
  File "/usr/lib/python3/dist-packages/dbus/proxies.py", line 250, in __init__
    self._named_service = conn.activate_name_owner(bus_name)
  File "/usr/lib/python3/dist-packages/dbus/bus.py", line 182, in activate_name_owner
    self.start_service_by_name(bus_name)
  File "/usr/lib/python3/dist-packages/dbus/bus.py", line 277, in start_service_by_name
    return (True, self.call_blocking(BUS_DAEMON_NAME, BUS_DAEMON_PATH,
  File "/usr/lib/python3/dist-packages/dbus/connection.py", line 652, in call_blocking
    reply_message = self.send_message_with_reply_and_block(
dbus.exceptions.DBusException: org.freedesktop.DBus.Error.TimedOut: Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
root@diya:~/pts-grpc# 
