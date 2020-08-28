import threading
from modules.client import Client
from modules.server import Server

def spool_up(doJoin):
    if doJoin:
        connectTo = input("Enter address (address:port): ")        
        if connectTo == "":
            connectTo = "2.tcp.ngrok.io:14583"
        host = connectTo.split(":")[0]
        port = connectTo.split(":")[1]
        print(host)
        print(port)
        myclient = Client(host, int(port))#change to whatever ngrok tunnels to
        client = threading.Thread(target=myclient.start, args=())
        client.start()
        client.join()
    myserver = Server("localhost", 8000)
    server = threading.Thread(target=myserver.start, args=())
    server.start()
    server.join()
