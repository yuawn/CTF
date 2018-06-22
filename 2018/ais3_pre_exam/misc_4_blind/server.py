#!/usr/bin/env python3
import os
from Crypto.Cipher import AES
from base64 import b64decode
from proof import proof

key = os.urandom(16)
answer = int.from_bytes(os.urandom(16), 'big')

with open("flag", 'r') as data:
    flag = data.read().strip()

def decrypt(text):
    iv, text = text[:16], text[16:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(text)

proof()

print("===== Welcome to number game =====")

while True:
    number = decrypt(b64decode(input("guess : ").strip()))[:16]
    number = int.from_bytes(number, 'big')
    if number > answer: print("Too big")
    elif number < answer: print("Too small")
    else: print(flag)


