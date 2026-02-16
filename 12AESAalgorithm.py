from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from crypto.util.padding import pad ,unpad

def encrypt_AES(key,plaintext):
    cipher=AES.new(key,AES.MODE_CBC)
    ciphertext=cipher.encrypt(pad(plaintext.encode(),AES.block_size))
    return ciphertext,cipher.iv

def decrypt_AES(key,ciphertext,iv):
    cipher=AES.new(key,AES.MODE_CBC,iv=iv)
    plaintext=unpad(cipher.decrypt(ciphertext),AES.block_size)
    return plaintext.decode()

key =get_random_bytes(16)
plaintext="hello world!"
ciphertext,iv = encrypt_AES(key,plaintext)
decrypted_text=decrypt_AES(key,ciphertext,iv)

print("plaintext:",plaintext)
print("ciphertext:",ciphertext)
print("decrypted text:",decrypted_text)