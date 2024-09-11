from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os

key = b'Sixteen byte key'

iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

message = b"This is a secret message."

ciphertext, tag = cipher.encrypt_and_digest(message)

with open('encrypted_message.bin', 'wb') as file:
    [file.write(x) for x in (iv, ciphertext, tag)]

print("Message encrypted and saved to 'encrypted_message.bin'")