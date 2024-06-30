                                LockBox

LockBox is a Python tool for encrypting files within a specified directory using the Fernet symmetric encryption scheme from the cryptography library.

Features:

    Encrypts files within a specified directory.
    Sends encrypted files and encryption keys to a specified server listener.
    Self-destruct feature: Deletes the script file and Key after execution.

Requirements

    Python 3.6+
    cryptography library



Usage:

Running the Tool

To encrypt files in the current directory and send them to the server:

    FOR LINUX DISTRO

    git clone https://github.com/your-username/lockbox.git

    cd lockbox

    pip install -r requirements.txt

    python malware.py

    FOR WINDOWS

    Download the Zip file and follow SAME STEPS:

    The script will encrypt files (excluding itself and specific files like encryption keys) and send them along with a newly generated encryption key (client_key.key) to the specified server.

    Additionally, it sends the encryption key to a listener for secure storage.


Notes:

    Encryption Key: The encryption key (server_key.key) generated during execution is sent to both the server and a listener for secure storage and decryption of files.
    Self-Destruct: Ensure that the script runs in a controlled environment as it deletes itself after execution.

Contributing

Contributions are welcome! If you find any bugs or have suggestions, please open an issue or create a pull request.
