import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
import base64

class InvalidPasswordError(Exception):
    pass

def derive_key(password: str, salt: bytes = b'static_salt'):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # CORRECT: cryptography's SHA256
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(input_path, output_path, password):
    key = derive_key(password)
    fernet = Fernet(key)
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_path, 'wb') as f:
        f.write(encrypted)

def decrypt_file(input_path, output_path, password):
    key = derive_key(password)
    fernet = Fernet(key)
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    try:
        decrypted = fernet.decrypt(encrypted_data)
    except InvalidToken:
        raise InvalidPasswordError("Invalid password or corrupted file.")
    with open(output_path, 'wb') as f:
        f.write(decrypted)

# Bonus: Folder encryption/decryption (optional)
def encrypt_folder(input_dir, output_dir, password):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename + '.enc')
        if os.path.isfile(input_path):
            encrypt_file(input_path, output_path, password)

def decrypt_folder(input_dir, output_dir, password):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.enc', '.dec.txt'))
        if os.path.isfile(input_path):
            decrypt_file(input_path, output_path, password)
