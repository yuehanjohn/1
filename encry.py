from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os

# Shared secret key (must be 16, 24, or 32 bytes long)
key = b'Sixteen byte key'

# Generate a random 16-byte IV
iv = get_random_bytes(16)

# Create the cipher
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

# The message to encrypt
message = b"This is a secret message."

# Encrypt the message
ciphertext, tag = cipher.encrypt_and_digest(message)

# Write the IV, ciphertext, and tag to a file
with open('encrypted_message.bin', 'wb') as file:
    [file.write(x) for x in (iv, ciphertext, tag)]

print("Message encrypted and saved to 'encrypted_message.bin'")