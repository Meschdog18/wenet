import socket


class Server():
    def __init__(self, host, port):
        self._host = host
        self._port = port
    
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_addr = (self._host, self._port)
        s.bind(server_addr)
        s.listen(1)



        while True:
            conn = None
            try:
                print("waiting for conn")
                conn, client_addr = s.accept()
                print("{} connected".format(client_addr))

                while True:
                    data = conn.recv(1024)
                    if data:
                        conn.sendall(data)
                    else:
                        break
            except KeyboardInterrupt:
                print("server shutdown")
                if conn:
                    conn.close()
        s.close()