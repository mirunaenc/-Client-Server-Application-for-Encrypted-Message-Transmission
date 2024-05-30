import socket
import json
from Common import is_prime, get_primitive_root, caesar_encrypt # type: ignore

def client_program():
    # Incarcam configuratia din fisierul JSON
    with open('config.json', 'r') as file:
        config = json.load(file)

    host = config['host']
    port = config['port']

    client_socket = socket.socket()
    client_socket.connect((host, port))

    q = int(input("Enter a prime number q: "))
    while not is_prime(q):
        q = int(input("q is not prime, try again: "))

    client_socket.send(str(q).encode())

    response = client_socket.recv(1024).decode()
    if response == 'q is not prime':
        print(response)
        client_socket.close()
        return

    primitive_root = int(response)
    Xa = int(input("Client, enter your secret key Xa (less than q): "))
    Ya = pow(primitive_root, Xa, q)
    client_socket.send(str(Ya).encode())

    Yb = int(client_socket.recv(1024).decode())
    shared_secret = pow(Yb, Xa, q)
    print(f"Shared encryption key K: {shared_secret}")

    while True:
        message = input("Enter message to send (type 'quit' to stop): ")
        if message.lower() == 'quit':
            break
        encrypted_message = caesar_encrypt(message, shared_secret)
        client_socket.send(encrypted_message.encode())

    client_socket.close()

if __name__ == '__main__':
    client_program()
