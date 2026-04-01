# Cryptography Toolkit

This was my first real Python project that actually felt useful. I built it during my CODEC Technologies internship to understand how cryptography actually works under the hood — not just what SHA-256 or RSA means in theory, but what happens when you actually run it.

It's a simple menu-driven terminal app.

## What it does

Three main things:

**Hashing** — type in any text, get back a SHA-256 or SHA-512 hash. The first time I ran this and saw the same input always produce the same output I understood why hashing is used for password storage. One-way, fixed length, no reversing it.

**AES Encryption (Symmetric)** — encrypt a message with a password, decrypt it with the same password. Built on AES-256 with PBKDF2 key derivation. Simple to use, strong algorithm.

**RSA Encryption (Asymmetric)** — generate a public/private key pair, encrypt with public key, decrypt with private key. This one took me the longest to understand but it clicked when I thought of it like a padlock — anyone can lock it, only you can open it.

## How to run it

```bash
pip install -r requirements.txt
python main.py
```

You'll get a numbered menu — pick an option and follow the prompts.

**Important:** Generate RSA keys first (Option 4) before trying RSA encryption. 

## Menu options

| Option | What it does |
|---|---|
| 1 | Hash any text — SHA-256 and SHA-512 |
| 2 | AES encrypt a message with a password |
| 3 | AES decrypt — needs same password |
| 4 | Generate RSA key pair — run this first |
| 5 | RSA encrypt using public key |
| 6 | RSA decrypt using private key |
| 7 | Exit |


## What I actually learned building this

The difference between hashing and encryption finally made sense when I built both in the same project. Hashing is one-way — you can verify but never reverse. Encryption is two-way — you can get the original back if you have the key.
Also learned the hard way that AES decryption fails silently if the password is wrong — spent 20 minutes debugging before I realised I was typing the password differently.
RSA has a message size limit — around 190 characters with RSA-2048. Anything longer breaks. That limitation alone explains why real systems use RSA to exchange a symmetric key, then switch to AES for the actual data.

## Tech used

- Python 3
- `cryptography` library — AES and hashing
- `pycryptodome` — RSA
- Algorithms: SHA-256, SHA-512, AES-256, RSA-2048 with OAEP padding, PBKDF2

## Common errors

**ModuleNotFoundError** — run `pip install -r requirements.txt`
**RSA keys not found** — run Option 4 first to generate keys
**AES decryption failed** — wrong password or encrypted text got corrupted during copy paste


## Honest limitations

This is a learning project, not production code. The key storage has no password protection, there's no GUI, and file encryption isn't supported yet. Maybe I'll add those later when I have time.

