import socket
from des import encrypt

HOST = "127.0.0.1"
PORT = 5000
KEY = b"12345678"

print("Legacy Bank Client")

transaction = input("Enter banking transaction: ")

plaintext = transaction.encode()
ciphertext = encrypt(plaintext, KEY)

print("\nOriginal transaction:", transaction)
print("Encrypted ciphertext:", ciphertext.hex())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(ciphertext)

print("Encrypted transaction sent to server.")
