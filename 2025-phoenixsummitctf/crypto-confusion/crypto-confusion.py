from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

FLAG = 'flag{fake-flag-for-testing}'
KEY = os.urandom(16)

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return ("plaintext = " + decrypted.hex() + "\n")


def encrypt(input: str):
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(input.encode(), AES.block_size))
    ciphertext = iv.hex() + encrypted.hex()

    return ("ciphertext = " + ciphertext + "\n")

print("""
      Welcome to the encryption/decryption service!
      """)
print("The secret", encrypt(FLAG))
print("1. Encrypt stuff")
print("2. Decrypt stuff\n")

while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(encrypt(input("Enter plaintext: ")))
        elif choice == 2:
            print(decrypt(input("Enter ciphertext: ")))
        else:
            break
    except:
        break
