import socket
import hmac
import hashlib

HOST = '0.0.0.0'
PORT = 12345
SECRET_KEY = b'shared_secret_key'

def verify_message(message, received_hmac):
    calculated_hmac = hmac.new(
        SECRET_KEY, message.encode(), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(calculated_hmac, received_hmac)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(4096).decode()
    if not data:
        break

    message, received_hmac = data.split("|")
    if message.lower() == "exit":
        break

    if verify_message(message, received_hmac):
        print("Client:", message)
        reply = input("You: ")
        reply_hmac = hmac.new(
            SECRET_KEY, reply.encode(), hashlib.sha256
        ).hexdigest()
        conn.send(f"{reply}|{reply_hmac}".encode())
    else:
        print("⚠️ Message integrity check failed!")

conn.close()
server.close()