import socket, threading
from cryptography.fernet import Fernet

KEY = b'gpRXckyXQyeRtZVEY_1e6U7TVR8iqHhT7d13KmsMrtQ='
cipher = Fernet(KEY)

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen()

clients = []

def broadcast(msg):
    for c in clients:
        try:
            c.send(cipher.encrypt(msg.encode()))
        except:
            pass

def handle(client):
    while True:
        try:
            data = client.recv(2048)
            msg = cipher.decrypt(data).decode()
            print("Received:", msg)   # debug
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break

print("Server running on port 5000...")

while True:
    c, addr = server.accept()
    print("Connected:", addr)
    clients.append(c)
    threading.Thread(target=handle, args=(c,), daemon=True).start()
