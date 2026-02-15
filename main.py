from hashE import sha256_hash, sha512_hash
from aes import encrypt_aes, decrypt_aes
from rsa import RSAEncryption
from colorama import Fore, Style, init

init(autoreset=True)

rsa = RSAEncryption()

def showheader():
    print("       CRYPTOGRAPHY TOOLKIT      ")
def show_menu():
    print("\n===== MENU =====")
    print("1. Hash Text")
    print("2. AES Encrypt")
    print("3. AES Decrypt")
    print("4. Generate RSA Keys")
    print("5. RSA Encrypt")
    print("6. RSA Decrypt")
    print("7. Exit")
def hashtext():
    print("\n--- Hash Text ---" )
    text = input("Enter text: ").strip()
    if not text:
        print("Text cannot be empty!")
        return
    print(f"\nOriginal: {text}")
    print(f"\nSHA-256: {sha256_hash(text)}")
    print(f"\nSHA-512: {sha512_hash(text)}")
    print( "\nNote: Hashes cannot be reversed!")

def aesencrypt():
    print("\n--- AES Encrypt ----")
    text = input("Enter text: ").strip()
    if not text:
        print( "Text cannot be empty")
        return
    
    password = input("Password (min 6 chars): ").strip()
    
    if len(password) < 6:
        print("Password too short")
        return
    
    result = encrypt_aes(text, password)
    print(f"\nEncrypted: {result}")

def aesdecrypt():
    print( "\n----- AES Decrypt ----" )
    encrypted = input("Encrypted text: ").strip()
    
    if not encrypted:
        print("Cannot be empty")
        return
    
    password = input("Password: ").strip()
    result = decrypt_aes(encrypted, password)
    
    if "Error" in result or "Wrong" in result:
        print(f"\n{result}" )
    else:
        print(f"\nDecrypted: {result}")

def generatersa():
    print( "\n--- Generate Keys ---")
    confirm = input("Overwrite existing keys? (yes or no): ").strip().lower()
    
    if confirm != 'yes':
        print("Cancelled")
        return
    result = rsa.generate_keys()
    print( f"\n{result}")

def rsaencrypt():
    print("\n--- RSA Encrypt -----" )
    text = input("Text (max 190 chars): ").strip()
    
    if not text:
        print("Cannot be empty")
        return
    
    if len(text) > 190:
        print("Text too long")
        return
    
    result = rsa.encrypt(text)
    
    if "Error" in result:
        print( f"\n{result}" )
    else:
        print(f"\nEncrypted: {result}")

def rsadecrypt():
    print( "\n------= RSA Decrypt ---")
    encrypted = input("Encrypted text: ").strip()
    
    if not encrypted:
        print("Cannot be empty")
        return
    
    result = rsa.decrypt(encrypted)
    
    if "Error" in result:
        print(f"\n{result}")
    else:
        print(f"\nDecrypted: {result}")

def main():
    showheader()
    
    while True:
        show_menu()
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            hashtext()
        elif choice == '2':
            aesencrypt()
        elif choice == '3':
            aesdecrypt()
        elif choice == '4':
            generatersa()
        elif choice == '5':
            rsaencrypt()
        elif choice == '6':
            rsadecrypt()
        elif choice == '7':
            print( "\nThank you!" )
            break
        else:
            print("\nInvalid choice!" )
        
if __name__ == "__main__":
    main()