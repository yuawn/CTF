#!/usr/bin/python2

from pwn import *
import base64
import sys
import re
import md5

def Stage2Decode(cipher):
    plain = ''
    for c in cipher:
        if c.isupper():
            c = chr(ord('A') + ord('Z') - ord(c))
        elif c.islower():
            c = chr(ord('a') + ord('z') - ord(c))
        plain += c
    return plain

def Stage3Decode(m0, c0, c1):   # Caesar Cipher
    m0 = re.sub(r"[^A-Za-z]", "", m0)
    c0 = re.sub(r"[^A-Za-z]", "", c0)
    key = ord(c0[0]) - ord(m0[0])
    m1 = ''
    for c in c1:
        if c.isupper():
            c = chr(((ord(c) - 65) % 26 - key) % 26 + 65)
        elif c.islower():
            c = chr(((ord(c) - 97) % 26 - key) % 26 + 97)
        m1 += c
    return m1

def Stage4Decode(m0, c0, c1):   # Vigenere Cipher
    m0 = re.sub(r"[^A-Za-z]", "", m0)
    c0 = re.sub(r"[^A-Za-z]", "", c0)
    i = 0
    repeat = 0
    j = 0
    key = []
    length = len(m0)
    while i < length:
        key.append( (ord(c0[i]) - ord(m0[i])) % 26 )
        if i != j and key[i] == key[j]:
            repeat = i - j
            j = j + 1
        elif repeat != 0 and key[i] != key[j]:
            repeat = 0
            j = 0
        i = i + 1
    key = key[0:repeat]
    m1 = ''
    i = 0
    for c in c1:
        if c.isupper():
            c = chr(((ord(c) - 65) % 26 - key[i]) % 26 + 65)
        elif c.islower():
            c = chr(((ord(c) - 97) % 26 - key[i]) % 26 + 97)
        else:
            i = i - 1
        m1 += c
        i = (i + 1) % len(key)
    return m1

def Stage5Decode(m0, c0, m1, c1, m2, c2, c3):   # Stream Cipher (XOR)
    if len(c0) == len(c3):
        return hex(int(c0, 16) ^ int(c3, 16) ^ int(m0, 16))[2:].decode('hex') + '\n'
    elif len(c1) == len(c3):
        return hex(int(c1, 16) ^ int(c3, 16) ^ int(m1, 16))[2:].decode('hex') + '\n'
    elif len(c2) == len(c3):
        return hex(int(c2, 16) ^ int(c3, 16) ^ int(m2, 16))[2:].decode('hex') + '\n'
    return '\n'

def Stage6Decode(m0, c0, c1):   # Transposition Cipher
    length = len(m0)
    key = 1
    de = list(c0)
    while key < length:
        i = 0
        j = 0
        k = i
        while j < length:
            de[i] = c0[j]
            i = i + key
            if i >= length:
                i = k + 1
                k = i
            j = j + 1
        if ''.join(de) == m0:
            break
        key = key + 1
    length = len(c1)
    de = list(c1)
    i = 0
    j = 0
    k = i
    while j < length:
        de[i] = c1[j]
        i = i + key
        if i >= length:
            i = k + 1
            k = i
        j = j + 1
    m1 = ''.join(de) + '\n'
    return m1

def Stage7Decode(cipher):   # MD5 hash
    pool = 'abcdefghijklmnopqrstuvwxyz 0123456789'
    for a in pool:
        for b in pool:
            for c in pool:
                for d in pool:
                    if md5.md5(a + b + c + d).hexdigest()[0:4] == cipher:
                        return a + b + c + d + '\n'
    return '\n'

conn = remote ('csie.ctf.tw', 10124)
treasure = ''

print (conn.recvuntil ('******** STAGE 0 ********'))

for i in range(3):
    print (conn.recvuntil (': '))
    cipher = conn.recvuntil ('\n', drop=True)
    print (cipher)
    plain = cipher.decode('hex') + '\n'
    print (plain)
    conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 1 ********'))

for i in range(3):
    print (conn.recvuntil (': '))
    cipher = conn.recvuntil ('\n', drop=True)
    print (cipher)
    plain = base64.b64decode (cipher) + '\n'
    print (plain)
    conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 2 ********'))

sys.stdout.write (conn.recvuntil ('c1 = '))
cipher = conn.recvline()
print (cipher)
print (conn.recvuntil('What is m1?'))
plain = Stage2Decode(cipher)
print (plain)
conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 3 ********'))

sys.stdout.write (conn.recvuntil ('m0 = '))
m0 = conn.recvuntil('\n', drop=True)
print (m0)
sys.stdout.write (conn.recvuntil ('c0 = '))
c0 = conn.recvuntil('\n', drop=True)
print (c0)
sys.stdout.write (conn.recvuntil ('c1 = '))
cipher = conn.recvline()
print (cipher)
print (conn.recvuntil('What is m1?'))
plain = Stage3Decode(m0, c0, cipher)
print (plain)
conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 4 ********'))

sys.stdout.write (conn.recvuntil ('m0 = '))
m0 = conn.recvuntil('\n', drop=True)
print (m0)
sys.stdout.write (conn.recvuntil ('c0 = '))
c0 = conn.recvuntil('\n', drop=True)
print (c0)
sys.stdout.write (conn.recvuntil ('c1 = '))
cipher = conn.recvline()
print (cipher)
print (conn.recvuntil('What is m1?'))
plain = Stage4Decode(m0, c0, cipher)
print (plain)
conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 5 ********'))

sys.stdout.write (conn.recvuntil ('m0 = '))
m0 = conn.recvuntil('\n', drop=True).encode('hex')
print (m0)
sys.stdout.write (conn.recvuntil ('c0 = '))
c0 = conn.recvuntil('\n', drop=True)
print (c0)
sys.stdout.write (conn.recvuntil ('m1 = '))
m1 = conn.recvuntil('\n', drop=True).encode('hex')
print (m1)
sys.stdout.write (conn.recvuntil ('c1 = '))
c1 = conn.recvuntil('\n', drop=True)
print (c1)
sys.stdout.write (conn.recvuntil ('m2 = '))
m2 = conn.recvuntil('\n', drop=True).encode('hex')
print (m2)
sys.stdout.write (conn.recvuntil ('c2 = '))
c2 = conn.recvuntil('\n', drop=True)
print (c2)
sys.stdout.write (conn.recvuntil ('c3 = '))
cipher = conn.recvuntil('\n', drop=True)
print (cipher)
print (conn.recvuntil('What is m3?'))
plain = Stage5Decode(m0, c0, m1, c1, m2, c2, cipher)
print (plain)
conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 6 ********'))

sys.stdout.write (conn.recvuntil ('m0 = '))
m0 = conn.recvuntil('\n', drop=True)
print (m0)
sys.stdout.write (conn.recvuntil ('c0 = '))
c0 = conn.recvuntil('\n', drop=True)
print (c0)
sys.stdout.write (conn.recvuntil ('c1 = '))
cipher = conn.recvuntil('\n', drop=True)
print (cipher)
print (conn.recvuntil('What is m1?'))
plain = Stage6Decode(m0, c0, cipher)
print (plain)
conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil ('******** STAGE 7 ********'))

for i in range(3):
    sys.stdout.write (conn.recvuntil ('MD5(m) = '))
    cipher = conn.recvuntil('\n', drop=True)
    print (cipher)
    print (conn.recvuntil('What is m?'))
    plain = Stage7Decode(cipher)
    print (plain)
    conn.send(plain)

conn.recvuntil('You got a piece of the treasure map: ')
treasure += conn.recvuntil('\n', drop=True)

print (conn.recvuntil('Congrats! Now you have all the pieces needed to recover the treasure.\n'))
print ("Here is your treasure:\n" + treasure);
