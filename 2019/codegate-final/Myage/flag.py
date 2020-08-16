#!/usr/bin/env python
from pwn import *
import base64 , re , os

# 
context.arch = 'amd64'
host , port = '110.10.147.114' , 40129
y = remote( host , port )

os.system( 'rm elf*' )


t = 0
ti = 0.1

def save_file():
    global t
    s = base64.b64decode( y.recvline() )
    o = open( './elf%d' % t , 'w+' )
    o.write( s )
    o.close()
    os.system( 'zlib-flate -uncompress < ./elf%d > elf' % ( t ) )
    return s

save_file()


y.interactive()