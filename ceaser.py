from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# generating key for cipher
salt = b'W\xd9\xaf5\xab\xf1pGW\xb2\x04\xd5"\xcb@\x93\x9aj\x1a\xedqb\x13+-\xf7\xf8?\xc6\xe4\xcb\x11'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"hello my name is ebad"

# generating cipher

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

# message converted to cipher
print(ciphered_data)

# file created containing characters that cannot be identified(encryption)
with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)


# decryption process
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
   
cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)


# original message decrypted after encryption
print(original)
