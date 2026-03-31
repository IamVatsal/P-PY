import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 1235
cs.connect((ip, port))

print("Connection from: " + ip)
print("type 'exit' for exit.")

while True:
    msg = cs.recv(1024).decode()
    if msg.lower() == "exit":
        print("Connection closed by the Server.")
        break
    print("Server> " + msg)
    msg = input("Client> ")
    cs.send(msg.encode())

cs.close()