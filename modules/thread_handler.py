import threading
from modules.client import Client
from modules.server import Server

def spool_up():
    myclient = Client("2.tcp.ngrok.io", 14583)#change to whatever ngrok tunnels to
    myserver = Server("localhost", 8000)

    client = threading.Thread(target=myclient.start, args=())
    server = threading.Thread(target=myserver.start, args=())

    client.start()
    server.start()

    client.join()
    server.join()