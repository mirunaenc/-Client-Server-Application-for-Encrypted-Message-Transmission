import socket
import json
from Common import is_prime, get_primitive_root, caesar_decrypt # type: ignore

def server_program():
    # Incarcam configuratia din fisierul JSON
    with open('config.json', 'r') as file:
        config = json.load(file)

    host = config['host']
    port = config['port']

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    q = int(conn.recv(1024).decode())
    if not is_prime(q):
        conn.send(b'q is not prime')
        conn.close()
        return

    primitive_root = get_primitive_root(q)
    conn.send(str(primitive_root).encode())

    Xb = int(input("Server, enter your secret key Xb (less than q): "))
    Yb = pow(primitive_root, Xb, q)
    conn.send(str(Yb).encode())

    Ya = int(conn.recv(1024).decode())
    shared_secret = pow(Ya, Xb, q)
    print(f"Shared encryption key K: {shared_secret}")

    while True:
        encrypted_message = conn.recv(1024).decode()
        if not encrypted_message:
            break
        print("Encrypted message received:", encrypted_message)
        decrypted_message = caesar_decrypt(encrypted_message, shared_secret)
        print("Decrypted message:", decrypted_message)

    conn.close()

if __name__ == '__main__':
    server_program()
