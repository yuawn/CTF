#!/usr/bin/env python
from pwn import *
from hashlib import sha256
import random , string

# AIS3{Spid3r mAn - H3L1O wOR1d PrO0F 0F WOrK}

host , port = '104.199.235.135' , 20000
y = remote( host , port )


y.recvuntil( '== \'' )
a = y.recv( 6 )
print a
y.recvuntil( '== \'' )
b = y.recv( 6 )
print b

p = range(48,58) + range(65,91) + range(97,123)

'''
sol = a + ''.join( random.choice( string.letters+string.digits ) for _ in xrange(16) )
while not sha256( sol ).hexdigest().startswith( b ):
    #print sol, sha256( sol ).hexdigest()
    sol = a + ''.join( random.choice( string.letters+string.digits ) for _ in xrange(16) )

print sol
'''
sol = ''

for i in xrange( 0x100000000 ):
    sol = a + str( i )
    if sha256( sol ).hexdigest().startswith( b ):
        break

y.sendline( sol )

y.interactive()