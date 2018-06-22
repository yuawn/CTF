#!/usr/bin/env python2
import os
import re
import random
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES


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
Here is your fla'sheep.ga/aaaaabbbbbbb}

--BOUNDARY
Type: text
Hope you like our crypto challenges.
Thanks for solving as always.
I'll catch you guys next time.
See ya!

--BOUNDARY
'''


def ex( s ):
    t = '-' * 0x30 + '\n'
    for i in xrange( len( s ) ):
        if not i % 16 and i:
            t += '\n'
        t += hex( ord( s[i] ) ).replace( '0x' , '' ).ljust( 2 , '0') + ' '
    return t + '\n' + '-' * 0x30

def ex2( s ):
    t = '-' * 0x30 + '\n'
    for i in xrange( len( s ) ):
        if not i % 16 and i:
            t += '\n'
        t += s[i] if s[i] != '\n' else '@'
    return t + '\n' + '-' * 0x30
    
print ex2( mod )
    
'''
key = b'\xa4\xcf\x03C0\x7f%\xaf\x13\xf6\xe3s;\xb64\xb5'
iv = b'\xd4\xe2I\x85\xe8l\xe0O`\x04IQ\xa1-\x10-'
aes = AES.new(key, AES.MODE_CBC, iv)

p = 'a' * 16 + 'b' * 16 + 'c' * 16 + 'd' * 16 + 'e' * 16

c = aes.encrypt( p )

print ex( c )

c = c[:16] + '\x57' + c[1:]

p2 = aes.decrypt( c )

print ex( p2 )
'''

