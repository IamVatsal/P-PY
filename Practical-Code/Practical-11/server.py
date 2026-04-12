import socket
import time

hostname = input("Enter the hostname or IP address of the server: ")
port = int(input("Enter the port number to connect to: "))

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((hostname, port))
ss.listen()
cs, addr = ss.accept()

print("Connection from: " + str(addr))

while True:
    msg = input("Server> ")
    cs.send(msg.encode())
    time.sleep(1)

    msg = cs.recv(1024).decode()
    if msg.lower() == "exit":
        print("Connection closed by the Client.")
        break
    print("Client> " + msg)

cs.close()