from Cryptodome.Cipher import AES

key = b'Sixteen byte key'

filename = 'encrypted_message.bin'

with open(filename, 'rb') as file:
    iv = file.read(16)
    ciphertext = file.read(-1)

tag = ciphertext[-16:]
ciphertext = ciphertext[:-16]

cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

try:
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    print("Decrypted message:", plaintext.decode())
except ValueError:
    print("Key incorrect or message corrupted")