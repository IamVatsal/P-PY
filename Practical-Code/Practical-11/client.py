import socket
import time

hostname = input("Enter the hostname or IP address of the server: ")
port = int(input("Enter the port number to connect to: "))

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(hostname)
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