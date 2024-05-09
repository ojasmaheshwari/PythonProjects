from app import App
from classes.server import Server
from threading import Thread

def main():
    app = App("Server Handler", (800, 500))

    server = Server(Server.getHostIp(), 1818)
    
    # Call server.listen() in a new thread
    Thread(target=server.listen, args=(5,), daemon=True).start()
    while True:
        if server.clients != []:
            print("Got a connection")
            print(server.clients)
            break
    
    app.mainloop()

if __name__ == '__main__':
    main()