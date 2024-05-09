import socket
from classes.client import Client

class Server():
    running = True
    clients = []
    client_count = 0
    def __init__(self, ip, port):
        self.socket = socket.socket()
        self.ip = ip
        self.port = port
        self.socket.bind((ip, port))
        print("Socket binded to port")
    
    def listen(self, max_connections: int):
        # Call using threads
        self.socket.listen(max_connections)
        while self.running:
            self.client_sock, self.client_address = self.socket.accept()
            self.client_count += 1

            self.client = Client(
                self.client_count,
                self.client_sock,
                self.client_address
            )
            self.clients.append(self.client)
        self.client_sock.close()
        
    @staticmethod
    def getHostIp():
        return socket.gethostbyname(socket.gethostname())
