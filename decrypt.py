#!/usr/bin/env python3

import os
import time
import random
from cryptography.fernet import Fernet, InvalidToken

# ANSI escape sequences for colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

files = []

file_name = "encrypt.py"

# List files in the current directory excluding specific files
for i in os.listdir():
    if i == file_name or i == "listener.py" or i == "decrypt.py" or i == "sample_decrypt.py" or i == "malware.py" or i=="server_key.key":
        continue
    if os.path.isfile(i):
        files.append(i)

# Function to print colored messages
def print_colored(msg, color):
    print(f"{color}{msg}{colors.END}")

# No password required for decryption, use server key directly
with open("server_key.key", "rb") as key_file:
    secretkey = key_file.read()

print_colored("[+] Decryption is under process...", colors.GREEN)

for file in files:
    try:
        with open(file, "rb") as f:
            content = f.read()
            cipher_suite = Fernet(secretkey)
            decrypted_content = cipher_suite.decrypt(content)
        
        with open(file, "wb") as f:
            f.write(decrypted_content)
        
        # Add a random delay between 1 to 10 seconds
        delay = random.randint(1, 10)
        # print_colored(f"[+] Decrypting {file}... (waiting {delay} seconds)", colors.YELLOW)
        time.sleep(delay)

    except InvalidToken as e:
        print_colored(f"[ERROR] Failed to decrypt {file}: {e}", colors.RED)

print_colored("Congrats, your files have been successfully decrypted!", colors.GREEN)
