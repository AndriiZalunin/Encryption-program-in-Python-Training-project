# Encryption program (Training project)
## Overview
The program allows you to encrypt and decrypt entered messages.
## More detailed
First, a single large string of various characters is created, which is then
converted into the first list. The second list is a copy of the first,
but the characters are randomly shuffled and will be used
for encryption.
```Python
import random
import string

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
#...
```
Then the user must enter a word/message. Using a loop,
an encrypted string is created for which characters are taken from the shuffled
list `keys`, whose index corresponds to the index of the character from the list `chars`
that was used by the user.
```Python
#...
#Encrypt
plain_text = input("Enter a message text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")
#...
```
The same method is used for decryption, but the lists are used
in reverse order.