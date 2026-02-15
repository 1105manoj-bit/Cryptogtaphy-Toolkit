Cryptography Toolkit 

A simple, menu-driven Python application that demonstrates core cryptographic concepts such as hashing, symmetric encryption, and asymmetric encryption.  
This project was developed as part of my cybersecurity internship at Codec Technologies to gain hands-on experience with cryptography algorithms.

Project Overview

This toolkit allows users to:
- Generate cryptographic hashes
- Encrypt and decrypt messages using AES (password-based encryption)
- Encrypt and decrypt messages using RSA (public/private key encryption)

The focus of this project is "learning and understanding cryptographic fundamentals", not production-grade security.

 Features Explained

1. Hashing
- Converts input text into a fixed-length hash
- Uses SHA-256 and SHA-512
- Hashes are one-way and cannot be reversed

- Commonly used for secure password storage
 2. AES Encryption (Symmetric)
- Encrypts text using a password
- Same password is required for decryption
- Uses AES-256 with a derived key
- Suitable for protecting private messages

 3. RSA Encryption (Asymmetric)
- Uses a public key to encrypt data
- Uses a private key to decrypt data
- RSA keys are generated and stored locally
- Demonstrates real-world public-key cryptography concepts

 Installation

 Requirements
- Python 3.7 or newer

Steps
1. Clone or download this repository  
2. Open a terminal in the project directory  
3. Install dependencies:

bash
pip install -r requirements.txt

Running the Program
python main.py

You will be shown a menu with numbered options.
Simply choose an option and follow the prompts.

Menu Options 

Option 1 – Hash Text
Enter any text
View SHA-256 and SHA-512 hashes
Hashes cannot be reversed

Option 2 – AES Encrypt
Enter a message
Enter a password (minimum 6 characters)
Receive encrypted output

Option 3 – AES Decrypt
Paste the encrypted text
Enter the same password
Original message is displayed

Option 4 – Generate RSA Keys
Generates a public and private key pair
Keys are saved in the keys/ folder
Required before RSA encryption or decryption

Option 5 – RSA Encrypt
Encrypts text using the public key
Message length is limited (approximately 190 characters)
Outputs encrypted text

Option 6 – RSA Decrypt
Decrypts text using the private key
Displays the original message

Option 7 – Exit
Safely closes the program

What I Learned from This Project

Through this project, I gained practical understanding of:
The difference between hashing and encryption
Symmetric vs asymmetric cryptography
AES and RSA use-cases
Password-based key derivation (PBKDF2)
File handling for cryptographic keys
Handling invalid input and runtime errors
Security limitations in beginner-level implementations

Technical Details

Languages & Libraries

Python 3
cryptography (AES and hashing)
pycryptodome (RSA)

Algorithms Used:

SHA-256, SHA-512
AES-256
RSA-2048 with OAEP padding
PBKDF2 (100,000 iterations)

Common Errors & Fixes
ModuleNotFoundError

Install dependencies using:
pip install -r requirements.txt

RSA keys not found

Generate keys first using Option 4
Then use RSA encryption or decryption options

AES decryption failed

Incorrect password entered
Encrypted text was copied incorrectly

Future Improvements

Possible enhancements include:
File encryption support
Graphical user interface (GUI)
Random salt generation for stronger security
Password-protected private keys
Support for additional cryptographic algorithms

Conclusion

This project helped me understand the practical implementation of core cryptographic concepts used in cybersecurity.
While it is not intended for real-world secure communication, it provided valuable hands-on experience with hashing, encryption techniques, and key management, strengthening my foundation in applied cryptography.
