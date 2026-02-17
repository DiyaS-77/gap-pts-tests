2026-02-17 15:41:36,998 | INFO | Command: /usr/local/bluez/dbus-1.12.20/bin/dbus-daemon --system --nopidfile
Output: 
2026-02-17 15:41:36,998 | INFO | D-Bus daemon started successfully.
2026-02-17 15:41:36,998 | INFO | Cleaning up existing bluetooth daemons...
2026-02-17 15:41:36,999 | INFO | Stopping running bluetoothd daemons...
2026-02-17 15:41:37,011 | INFO | Command: killall -9 bluetoothd
Output: 
2026-02-17 15:41:37,012 | INFO | Successfully stopped bluetoothd daemon processes.
Traceback (most recent call last):
  File "server.py", line 33, in <module>
    serve()
  File "server.py", line 22, in serve
    remote_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
  File "/root/pts-grpc/stub_bluetooth.py", line 101, in __init__
    self._setup_logging()
  File "/root/pts-grpc/stub_bluetooth.py", line 112, in _setup_logging
    start_bluetooth_daemon(logger)
  File "/root/pts-grpc/Utils/utils.py", line 219, in start_bluetooth_daemon
    bluetoothd_log_name = os.path.join(log.log_path, "bluetoothd.log")
AttributeError: 'Logger' object has no attribute 'log_path'
root@diya:~/pts-grpc# 
