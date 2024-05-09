client = {}

def initialWhoisQuery(c):
    global client
    client = c
    client_socket = client[0]
    print("Init query: ", client_socket)
    client_socket.send("INITIAL_WHOAMI".encode())
    return client_socket.recv(1024).decode()

def printClient():
    if client != {}:
        pass
    else:
        print("client object is empty!!")

def sendCommand(cmd):
    print(f"Sending {cmd} to {client[1]}")
    client_socket = client[0]
    print(client_socket)
    client_socket.send("pwd".encode())
    output = client_socket.recv(1024).decode()
    return output