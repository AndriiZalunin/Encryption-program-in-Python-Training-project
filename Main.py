import random
import string

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

#print(chars)
#print(keys)

#Encrypt
plain_text = input("Enter a message text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#Decrypt
cipher_text = input("Enter a message text to be decrypted: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")