import socket
import hmac
import hashlib

HOST = '127.0.0.1'
PORT = 12345
SECRET_KEY = b'shared_secret_key'

def create_hmac(message):
    return hmac.new(
        SECRET_KEY, message.encode(), hashlib.sha256
    ).hexdigest()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to server.")

while True:
    msg = input("You: ")
    msg_hmac = create_hmac(msg)
    client.send(f"{msg}|{msg_hmac}".encode())

    if msg.lower() == "exit":
        break

    data = client.recv(4096).decode()
    reply, reply_hmac = data.split("|")

    if create_hmac(reply) == reply_hmac:
        print("Server:", reply)
    else:
        print("⚠️ Integrity check failed! Message tampered.")

client.close()