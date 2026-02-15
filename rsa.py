from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

class RSAEncryption:
    def __init__(self):
        self.key_folder = "keys"
        self.private_path = f"{self.key_folder}/private.pem"
        self.public_path = f"{self.key_folder}/public.pem"
        
        if not os.path.exists(self.key_folder):
            os.makedirs(self.key_folder)
    
    def generate_keys(self):
        try:
            key = RSA.generate(2048)
            private_key = key.export_key()
            public_key = key.publickey().export_key()
            
            with open(self.private_path, "wb") as f:
                f.write(private_key)
            
            with open(self.public_path, "wb") as f:
                f.write(public_key)
            
            return "Keys generated successfully!"
        except Exception as e:
            return f"Error: {e}"
    
    def get_public_key(self):
        try:
            with open(self.public_path, "rb") as f:
                return RSA.import_key(f.read())
        except:
            return None
    
    def get_private_key(self):
        try:
            with open(self.private_path, "rb") as f:
                return RSA.import_key(f.read())
        except:
            return None
    
    def encrypt(self, message):
        try:
            pub_key = self.get_public_key()
            if not pub_key:
                return "Error: Generate keys first!"
            
            cipher = PKCS1_OAEP.new(pub_key)
            encrypted = cipher.encrypt(message.encode())
            return base64.b64encode(encrypted).decode()
        except Exception as e:
            return f"Error: {e}"
    
    def decrypt(self, encrypted_msg):
        try:
            priv_key = self.get_private_key()
            if not priv_key:
                return "Error: Generate keys first!"
            
            cipher = PKCS1_OAEP.new(priv_key)
            enc_bytes = base64.b64decode(encrypted_msg)
            decrypted = cipher.decrypt(enc_bytes)
            return decrypted.decode()
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    print("=== RSA Test ===\n")
    
    rsa = RSAEncryption()
    print(rsa.generate_keys())
    
    msg = input("\nMessage (max 190 chars): ")
    enc = rsa.encrypt(msg)
    print(f"\nEncrypted: {enc}")
    
    dec = rsa.decrypt(enc)
    print(f"Decrypted: {dec}")