#!/usr/bin/env python
from pwn import *

# AIS3{G0_gO_g0_T0_h1Gh_!!!_R3v3rs3_oN_g0lauG_p1narY_1s_3xHanst3d_Orz}

host , port = '104.199.235.135' , 2115
y = remote( host , port )
#y = process( './calc' )

y.sendlineafter( '>' , '1' )
k1 = '\xff\x6d\xff\x07\x6f\x58\x10\x10\x70\x10\x30\x10\x10\x00\xff\x10\x30\x10\x20\x30\x26\x10\x30\x10\x6d'.ljust( 25 , '\x00' )
k2 = '\x00\x00\x00\x08\x00\x00\x10\x21\x03\x10\x44\x38\x20\x00\x00\x43\x44\x10\x43\x24\x20\x10\x44\x2a\x00'.ljust( 25 , '\x00' )
y.sendlineafter( '>' , k1 )
y.sendlineafter( '>' , k2 )

y.sendlineafter( '>' , '2' )

'''

0x0000006d0000fffd	0x0000000f0000fffd
0xc420041d9c:	0x000000580000006f	0x0000003100000020
0xc420041dac:	0x0000002000000073	0x0000004800000074

0xc420041dbc:	0x0000000000000030	0x000000530000fffd

0xc420041dcc:	0x0000002000000074	0x0000005400000063
0xc420041ddc:	0x0000002000000046	0x0000003a00000074
0000006d

b *0x493d60
b *0x493d8c
b *0x493d94
b *0x493d9d
'''


y.interactive()