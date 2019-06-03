#!/usr/bin/env python
from z3 import *
from pwn import *

# OOO{pox&mpuzz,U_solve_it => pHd_1w_e4rL13r;)}

s = Solver()

l = 10
flag = []

for i in range( l ):
  flag.append( BitVec( "flag_" + str( i ) , 32 ) )
  #s.add( flag[i] & 0xff > 0x1f )
  #s.add( flag[i] & 0xff < 128 )
  #s.add( ( flag[i] & 0xff00 ) >> 8 > 0x1f )
  #s.add( ( flag[i] & 0xff00 ) >> 8 < 128 )
  #s.add( ( flag[i] & 0xff0000 ) >> 16 > 0x1f )
  #s.add( ( flag[i] & 0xff0000 ) >> 16 < 128 )
  #s.add( ( flag[i] & 0xff000000 ) >> 24 > 0x1f )
  #s.add( ( flag[i] & 0xff000000 ) >> 24 < 128 )


s.add( flag[0] ^ flag[1] ^ flag[2] ^ flag[3] ^ flag[4] ^ flag[5] ^ flag[6] ^ flag[7] ^ flag[8] ^ flag[9] == 53412119 )
s.add( flag[1] ^ flag[3] ^ flag[5] ^ flag[7] ^ flag[9] == 1615013692 )
s.add( flag[2] ^ flag[5] ^ flag[8] == 1311204206 )
s.add( flag[3] ^ flag[7] == 322115650 )
s.add( flag[4] ^ flag[9] == 1565666646 )
s.add( flag[5] == u32( ' => ' ) )
s.add( flag[6] == u32( 'pHd_' ) )
s.add( flag[7] == u32( '1w_e' ) )
s.add( flag[8] == u32( '4rL1' ) )
s.add( flag[9] == u32( '3r;)' ) )


'''
OOO{pox&mpuzz,U_solve_it => pHd_1w_e4rL13r;)}
OOO{gnW%zqZyz,U_solve_it => pHd_1w_e4rL13r;)}
e_it => pHd_1w_e4rL13r;)}
'''

print s.check()

o = ''
ans = []
for i in range( l ):
    ans.append( s.model()[ flag[i] ].as_long() )
    o += p32( ans[i] )

print o