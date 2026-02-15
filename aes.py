from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64

def makekey(password):
    salt = b'my_salt_for_encryption_2024'
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_aes(text, password):
    try:
        key = makekey(password)
        cipher = Fernet(key)
        encrypted = cipher.encrypt(text.encode())
        return encrypted.decode()
    except Exception as e:
        return f"Error: {e}"

def decrypt_aes(encrypted_text, password):
    try:
        key = makekey(password)
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted_text.encode())
        return decrypted.decode()
    except Exception as e:
        return f"Wrong password or corrupted data"

if __name__ == "__main__":
    print("=== AES Test ===\n")
    
    original = input("Text to encrypt: ")
    pwd = input("Password: ")
    
    enc = encrypt_aes(original, pwd)
    print(f"\nEncrypted: {enc}")
    
    pwd2 = input("\nPassword to decrypt: ")
    dec = decrypt_aes(enc, pwd2)
    print(f"Decrypted: {dec}")