Traceback (most recent call last):
  File "server.py", line 33, in <module>
    serve()
  File "server.py", line 22, in serve
    remote_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
  File "/root/pts-grpc/stub_bluetooth.py", line 102, in __init__
    os.makedirs(log_path, exist_ok=True)
  File "/usr/lib/python3.8/os.py", line 208, in makedirs
    head, tail = path.split(name)
  File "/usr/lib/python3.8/posixpath.py", line 103, in split
    p = os.fspath(p)
TypeError: expected str, bytes or os.PathLike object, not NoneType
root@diya:~/pts-grpc# 


