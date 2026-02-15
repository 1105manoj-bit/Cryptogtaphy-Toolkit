import hashlib

def sha256_hash(text):
    try:
        hashobj = hashlib.sha256(text.encode())
        return hashobj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def sha512_hash(text):
    try:
        hashobj = hashlib.sha512(text.encode())
        return hashobj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("==== Hash Module Test ===\n")
    text = input("Enter text: ")
    
    print(f"\nOriginal: {text}")
    print(f"SHA-256: {sha256_hash(text)}")
    print(f"SHA-512: {sha512_hash(text)}")