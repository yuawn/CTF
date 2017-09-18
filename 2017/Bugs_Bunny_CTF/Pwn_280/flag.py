#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# 

host , port = '54.153.19.139' , 5258
host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF( 'pwn280' )

p = ''


y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()