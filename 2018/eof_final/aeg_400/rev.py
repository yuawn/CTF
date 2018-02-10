#!/usr/bin/env python
from pwn import *
import base64

# FLAG{FindBufferOverflowAmongTensofFunctions}

host , port = '10.141.0.202' , 8989
y = remote( host , port )

y.sendlineafter( '(y/n)' , 'y' )
y.recvuntil( 'Base64 =================' )
for _ in xrange( 2 ): y.recvline()

o = open( './tmp' , 'w+' )
o.write( base64.b64decode( y.recvline() ) )
o.close()


y.interactive()