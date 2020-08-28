import threading
from modules.client import Client
from modules.server import Server

def spool_up():
    connectTo = input("Enter address (address:port): ")
    if connectTo == "":
        connectTo = "2.tcp.ngrok.io:14583"
    host = connectTo.split(":")[0]
    port = connectTo.split(":")[1]
    myclient = Client(host, int(port))
    myserver = Server("localhost", 8000)

    client = threading.Thread(target=myclient.start, args=())
    server = threading.Thread(target=myserver.start, args=())

    client.start()
    server.start()

    client.join()
    server.join()
