#!/usr/bin/env python2
import os
import re
import random
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES

key = b'\xa4\xcf\x03C0\x7f%\xaf\x13\xf6\xe3s;\xb64\xb5'
iv = b'\xd4\xe2I\x85\xe8l\xe0O`\x04IQ\xa1-\x10-'

mail = '''
From: thor@ais3.org
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
Here is your flag : AIS3{abcdefg}

--BOUNDARY
Type: text
Hope you like our crypto challenges.
Thanks for solving as always.
I'll catch you guys next time.
See ya!

--BOUNDARY
'''

p = [ ord( i ) for i in mail ]


aes = AES.new(key, AES.MODE_CBC, iv)
c = aes.encrypt( mail )
c = [ ord( i ) for i in c ]
#print c , len(c)

for i in xrange( 16 , len( p ) , 16 ):
    s = ''
    print hex(i)
    for j in xrange( 16 ):
        if chr( p[ i + j ] ) == '\n':
            s += ' ' + '@' + ' '
        else:
            s += ' ' + chr( p[ i + j ] ) + ' '
    s += '\n'
    for j in xrange( 16 ):
        s += hex( c[ i + j - 16 ] ).replace( '0x' , '' ).rjust( 2 , '0' ) + ' '
    print s
    

