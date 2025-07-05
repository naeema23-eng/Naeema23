"""
File: file_encryptor_improved.py
Description: Improved file encryption and decryption tool with better error handling, testability, and flexible output paths.
"""

from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib


# Generate a key from a password using SHA-256
def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())


# Load file content
def load_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as file:
        return file.read()


# Save file content
def save_file(file_path: str, data: bytes):
    with open(file_path, 'wb') as file:
        file.write(data)


# Encrypt data
def encrypt_data(data: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    return fernet.encrypt(data)


# Decrypt data
def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)


# Encrypt a file
def encrypt_file(input_file: str, output_file: str, password: str):
    try:
        key = generate_key(password)
        data = load_file(input_file)
        encrypted_data = encrypt_data(data, key)
        save_file(output_file, encrypted_data)
        print(f"[+] File '{input_file}' encrypted successfully as '{output_file}'")
    except FileNotFoundError:
        print(f"[-] File '{input_file}' not found.")
        raise
    except Exception as e:
        print(f"[-] Error during encryption: {e}")
        raise


# Decrypt a file
def decrypt_file(input_file: str, output_file: str, password: str):
    try:
        key = generate_key(password)
        encrypted_data = load_file(input_file)
        decrypted_data = decrypt_data(encrypted_data, key)
        save_file(output_file, decrypted_data)
        print(f"[+] File '{input_file}' decrypted successfully as '{output_file}'")
        print("[Decrypted Content Preview]:")
        print(decrypted_data.decode())
    except InvalidToken:
        print("[-] Incorrect password or corrupted file.")
        raise
    except FileNotFoundError:
        print(f"[-] File '{input_file}' not found.")
        raise
    except Exception as e:
        print(f"[-] Error during decryption: {e}")
        raise


# Main CLI interface
if __name__ == "__main__":
    print("=== Improved File Encryption Tool (Python) ===")
    choice = input("Choose [E]ncrypt or [D]ecrypt: ").strip().lower()

    if choice == 'e':
        input_file = input("Enter the input file name (with extension): ").strip()
        output_file = input("Enter the output encrypted file name (with extension): ").strip()
        password = input("Enter password: ").strip()
        encrypt_file(input_file, output_file, password)

    elif choice == 'd':
        input_file = input("Enter the encrypted file name (with extension): ").strip()
        output_file = input("Enter the output decrypted file name (with extension): ").strip()
        password = input("Enter password: ").strip()
        decrypt_file(input_file, output_file, password)

    else:
        print("[-] Invalid choice. Please choose 'E' or 'D'.")


