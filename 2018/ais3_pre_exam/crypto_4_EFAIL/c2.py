#!/usr/bin/env python
import os
import re
import random
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

flag = 'AIS3{aaaaaabbbbbbb}'

# simplify mail format
mail_for_ctfplayer = '''From: thor@ais3.org
To: ctfplayer@ais3.org

--BOUNDARY
Type: text
Welcome to AIS3 pre-exam.

--BOUNDARY
Type: cmd
echo 'This is the blog of oalieno'
web 'https://oalieno.github.io'
echo 'This is the blog of bamboofox team'
web 'https://bamboofox.github.io/'

--BOUNDARY
Type: text
You can find some useful tutorial on there.
And you might be wondering where is the flag?
Just hold tight, and remember that patient is virtue.

--BOUNDARY
Type: text
Here is your flag : {}

--BOUNDARY
Type: text
Hope you like our crypto challenges.
Thanks for solving as always.
I'll catch you guys next time.
See ya!

--BOUNDARY
'''.format(flag)

mod = '''From: thor@ais3.org
To: ctfplayer@ais3.org

--BOUNDARY
Type: text
Welcome to AIS3 pre-exam.

--BOUNDARY
Type: cmd
echo 'This is the blog of oalieno'
web 'https://oalieno.github.io'
echo 'This is the blog of bamboofox team'
web 'https://bamboofox.github.io/'

--BOUNDARY
Type: text
You can find some useful tutorial on there.
And you might be wondering where is the flag?
Just hold tight, and remember

--BOUNDARY
 is virtue.

--BOUNType: cmd
webxt
Here is your fla'sheep.ga/'''



key = os.urandom(16)
iv = os.urandom(16)

def pad(text):
    L = -len(text) % 16
    return text + chr(L) * L

def unpad(text):
    L = text[-1]
    if L > 16:
        raise ValueError
    for i in range(1, L + 1):
        if text[-i] != L:
            raise ValueError
    return text[:-L]



aes = AES.new(key, AES.MODE_CBC, iv)
c = aes.encrypt(pad(mail_for_ctfplayer))
p = [ ord(i) for i in mail_for_ctfplayer ]
c = [ ord(i) for i in c ]
m = [ ord(i) for i in mod ]

for i in range( len( m ) ):
    #print( p[i] , m[i] )
    if p[i] != m[i]:
        #print chr(p[i]) , chr(m[i])
        c[i-16] = c[i-16] ^ p[i] ^ m[i]

ci = ''.join( chr( i ) for i in c )
print ci
plain = aes.decrypt( ci )
print plain

'''
p = [ i for i in mail_for_ctfplayer ]
c = [ i for i in c ]
m = [ i for i in mod ]

for i in range( len( m ) ):
    #print( p[i] , m[i] )
    if p[i] != m[i]:
        print( chr(p[i]) , chr(m[i]) )
        c[i-16] = c[i-16] ^ p[i] ^ m[i]

ci = bytes( c )

plain = aes.decrypt( ci )
print( plain )
parse_mail( plain )
'''