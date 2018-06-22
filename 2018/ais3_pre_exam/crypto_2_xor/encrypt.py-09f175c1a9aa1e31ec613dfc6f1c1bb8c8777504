#!/usr/bin/env python3
import os
import random

with open('flag', 'rb') as data:
    flag = data.read()
    assert(flag.startswith(b'AIS3{'))

def extend(key, L):
    kL = len(key)
    return key * (L // kL) + key[:L % kL]

def xor(X, Y):
    return bytes([x ^ y for x, y in zip(X, Y)])

key = os.urandom(random.randint(8, 12))
plain = flag + key
key = extend(key, len(plain))
cipher = xor(plain, key)

with open('flag-encrypted', 'wb') as data:
    data.write(cipher)
