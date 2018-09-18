#!/usr/bin/env python
from z3 import *

# TMCTF{SlytherinPastTheReverser}

s=[ BitVec('vec%d' % i , 8) for i in range(24) ]
rs = list( reversed( s ) )
solver = Solver()

def m32( i ):
    return ord( i ) - 32

def m8( i ):
    return ord( i ) - 8

def m1( i ):
    return ord( i ) - 1


v0 = map( m32 , 'R) +6' )
v1 = map( ord , 'l1:C(' )
v2 = map( m32 , ' RP%A' )
v3 = [ 236, 108, 102, 169, 93 ]
v4 = map( m32 , ' L30Z' )
v5 = map( m8 , ' j36~' )
v6 = map( m32 , ' M2S+' )
v7 = map( ord , '4e\x9c{E' )
v8 = map( m32 , '6!2$D' )
v9 = map( m1 , ']PaSs' )

solver.add( s[0] != 187 )
solver.add( s[0+0] ^ s[0+1] ^ s[0+2] ^ s[0+3] == v0[0] )
solver.add( s[0+0] + s[0+1] + s[0+2] + s[0+3] == v1[0] )
solver.add( s[0*0] ^ s[0*1] ^ s[0*2] ^ s[0*3] == v2[0] )
solver.add( s[0*0] + s[0*1] + s[0*2] + s[0*3] == v3[0] )
solver.add( s[8+0*0] ^ s[8+0*1] ^ s[8+0*2] ^ s[8+0*3] == v4[0] )
solver.add( s[8+0*0] + s[8+0*1] + s[8+0*2] + s[8+0*3] == v5[0] )
solver.add( rs[8+0*0] ^ rs[8+0*1] ^ rs[8+0*2] ^ rs[8+0*3] == v6[0] )
solver.add( rs[8+0*0] + rs[8+0*1] + rs[8+0*2] + rs[8+0*3] == v7[0] )
solver.add( rs[0+0] ^ rs[0+1] ^ rs[0+2] ^ rs[0+3] == v8[0] )
solver.add( rs[0+0] + rs[0+1] + rs[0+2] + rs[0+3] == v9[0] )
solver.add( s[1+0] ^ s[1+1] ^ s[1+2] ^ s[1+3] == v0[1] )
solver.add( s[1+0] + s[1+1] + s[1+2] + s[1+3] == v1[1] )
solver.add( s[1*0] ^ s[1*1] ^ s[1*2] ^ s[1*3] == v2[1] )
solver.add( s[1*0] + s[1*1] + s[1*2] + s[1*3] == v3[1] )
solver.add( s[8+1*0] ^ s[8+1*1] ^ s[8+1*2] ^ s[8+1*3] == v4[1] )
solver.add( s[8+1*0] + s[8+1*1] + s[8+1*2] + s[8+1*3] == v5[1] )
solver.add( rs[8+1*0] ^ rs[8+1*1] ^ rs[8+1*2] ^ rs[8+1*3] == v6[1] )
solver.add( rs[8+1*0] + rs[8+1*1] + rs[8+1*2] + rs[8+1*3] == v7[1] )
solver.add( rs[1+0] ^ rs[1+1] ^ rs[1+2] ^ rs[1+3] == v8[1] )
solver.add( rs[1+0] + rs[1+1] + rs[1+2] + rs[1+3] == v9[1] )
solver.add( s[2+0] ^ s[2+1] ^ s[2+2] ^ s[2+3] == v0[2] )
solver.add( s[2+0] + s[2+1] + s[2+2] + s[2+3] == v1[2] )
solver.add( s[2*0] ^ s[2*1] ^ s[2*2] ^ s[2*3] == v2[2] )
solver.add( s[2*0] + s[2*1] + s[2*2] + s[2*3] == v3[2] )
solver.add( s[8+2*0] ^ s[8+2*1] ^ s[8+2*2] ^ s[8+2*3] == v4[2] )
solver.add( s[8+2*0] + s[8+2*1] + s[8+2*2] + s[8+2*3] == v5[2] )
solver.add( rs[8+2*0] ^ rs[8+2*1] ^ rs[8+2*2] ^ rs[8+2*3] == v6[2] )
solver.add( rs[8+2*0] + rs[8+2*1] + rs[8+2*2] + rs[8+2*3] == v7[2] )
solver.add( rs[2+0] ^ rs[2+1] ^ rs[2+2] ^ rs[2+3] == v8[2] )
solver.add( rs[2+0] + rs[2+1] + rs[2+2] + rs[2+3] == v9[2] )
solver.add( s[3+0] ^ s[3+1] ^ s[3+2] ^ s[3+3] == v0[3] )
solver.add( s[3+0] + s[3+1] + s[3+2] + s[3+3] == v1[3] )
solver.add( s[3*0] ^ s[3*1] ^ s[3*2] ^ s[3*3] == v2[3] )
solver.add( s[3*0] + s[3*1] + s[3*2] + s[3*3] == v3[3] )
solver.add( s[8+3*0] ^ s[8+3*1] ^ s[8+3*2] ^ s[8+3*3] == v4[3] )
solver.add( s[8+3*0] + s[8+3*1] + s[8+3*2] + s[8+3*3] == v5[3] )
solver.add( rs[8+3*0] ^ rs[8+3*1] ^ rs[8+3*2] ^ rs[8+3*3] == v6[3] )
solver.add( rs[8+3*0] + rs[8+3*1] + rs[8+3*2] + rs[8+3*3] == v7[3] )
solver.add( rs[3+0] ^ rs[3+1] ^ rs[3+2] ^ rs[3+3] == v8[3] )
solver.add( rs[3+0] + rs[3+1] + rs[3+2] + rs[3+3] == v9[3] )
solver.add( s[4+0] ^ s[4+1] ^ s[4+2] ^ s[4+3] == v0[4] )
solver.add( s[4+0] + s[4+1] + s[4+2] + s[4+3] == v1[4] )
solver.add( s[4*0] ^ s[4*1] ^ s[4*2] ^ s[4*3] == v2[4] )
solver.add( s[4*0] + s[4*1] + s[4*2] + s[4*3] == v3[4] )
solver.add( s[8+4*0] ^ s[8+4*1] ^ s[8+4*2] ^ s[8+4*3] == v4[4] )
solver.add( s[8+4*0] + s[8+4*1] + s[8+4*2] + s[8+4*3] == v5[4] )
solver.add( rs[8+4*0] ^ rs[8+4*1] ^ rs[8+4*2] ^ rs[8+4*3] == v6[4] )
solver.add( rs[8+4*0] + rs[8+4*1] + rs[8+4*2] + rs[8+4*3] == v7[4] )
solver.add( rs[4+0] ^ rs[4+1] ^ rs[4+2] ^ rs[4+3] == v8[4] )
solver.add( rs[4+0] + rs[4+1] + rs[4+2] + rs[4+3] == v9[4] )

print solver.check()
ans = solver.model()
flag = ''.join( chr( ans[ _ ].as_long() ^ ord( 'h' ) ) for _ in s )
print 'TMCTF{%s}' % flag