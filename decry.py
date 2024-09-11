from Cryptodome.Cipher import AES

# Shared secret key (must be the same as in the encryption script)
key = b'Sixteen byte key'

# Name of the file to decrypt
filename = 'encrypted_message.bin'

# Read the file
with open(filename, 'rb') as file:
    iv = file.read(16)
    ciphertext = file.read(-1)

# Split ciphertext and tag
tag = ciphertext[-16:]
ciphertext = ciphertext[:-16]

# Create the cipher
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

# Decrypt the message
try:
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    print("Decrypted message:", plaintext.decode())
except ValueError:
    print("Key incorrect or message corrupted")