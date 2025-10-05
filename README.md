# Encryption program (Training project)
## Overview
Программа позволяет зашифровывать и расшифровывать введённые сообщения.
## More detailed
Сначала создается одна большая строка различных символов, которые потом
преобразовываются в первый список. Второй список является копией первого,
при этом перемешиваются случайным образом и будут использоватися
для шифрования.
```Python
import random
import string

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
#...
```
Потом пользователь должен ввести слово/сообщение. С помощью цикла
создается зашифрованная строка для котой берутся символы из перемешанного
списка `keys` индекс которых соответствует индексу символа из списка `chars`
которые были использованы пользователем.
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
Для дешифрования применяется такой же метод, но списки используются
наоборот.