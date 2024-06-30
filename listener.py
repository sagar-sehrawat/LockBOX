import socket
import os
from cryptography.fernet import Fernet

# Server configuration
SERVER_HOST = '192.168.172.96'  # Replace with your server's IP address
SERVER_PORT = 8888  # Choose any free port number

def print_banner():
    banner = """
██████╗ ███████╗███╗   ██╗███████╗███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝████╗  ██║██╔════╝████╗ ████║██╔══██╗████╗  ██║
██║  ██║█████╗  ██╔██╗ ██║█████╗  ██╔████╔██║███████║██╔██╗ ██║
██║  ██║██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║
██████╔╝███████╗██║ ╚████║███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                   
             LockBox v1.0
       ========================
         Author: Sagar Sehrawat
    """
    # Print banner with blue color
    print_colored(banner, colors.BLUE)

def receive_key():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}")
        
        client_socket, client_address = server_socket.accept()
        key = client_socket.recv(1024)
        
        # Save the key to a file
        with open("server_key.key", "wb") as key_file:
            key_file.write(key)
        
        print("[KEY RECEIVED] Key received and saved.")
        client_socket.close()
        server_socket.close()
        return key
    except Exception as e:
        print(f"[ERROR] Failed to receive key: {e}")
        return None

def receive_file(filename, key):
    cipher_suite = Fernet(key)
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print(f"[LISTENING] Server is listening on {SERVER_HOST}:{SERVER_PORT}")
        
        client_socket, client_address = server_socket.accept()
        with open(filename, 'wb') as f:
            while True:
                encrypted_data = client_socket.recv(1024)
                if not encrypted_data:
                    break
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                f.write(decrypted_data)
        
        print(f"[FILE RECEIVED] File '{filename}' received and saved.")
        client_socket.close()
        server_socket.close()
    except Exception as e:
        print(f"[ERROR] Failed to receive file: {e}")

if __name__ == "__main__":
    key = receive_key()
    if key:
        filename = input("Enter filename to save: ")
        receive_file(filename, key)
