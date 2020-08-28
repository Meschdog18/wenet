import socket

import time
class Client():
    def __init__(self, host, port):
        self._host = host
        self._port = port
    def start(self):
        time.sleep(5)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._host, self._port))
            s.sendall(b'hello')
            data = s.recv(1024)

        print('Received', repr(data))