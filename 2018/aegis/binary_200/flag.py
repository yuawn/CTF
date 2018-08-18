#!/usr/bin/env python
#import angr
import angr
from pwn import *
import base64 , re

# AEGIS{y0u_have_to_have_3B9L4_to_kn0w_DA_WAE_my_br00das}

host = '203.66.68.95'
port = 44544
y = remote( host , port )

y.sendafter( '...' , '\n' )
o = open( './tmp' , 'w+' )
o.write( base64.b64decode( y.recvuntil( '==' ) ) )
o.close()

p = angr.Project( './tmp' , load_options={'auto_load_libs': False} )

state = p.factory.entry_state( )

sm = p.factory.simulation_manager( state , immutable = False )

sm.explore( find = 0x400b05 )

a = 0x602140
b = 0x602210

ad = u64( sm.found[0].solver.eval( sm.found[0].memory.load( a , 8 ) , cast_to = str ) )

ch = sm.found[0].solver.eval( sm.found[0].memory.load( b , 26 ) , cast_to = str )

key = []

for i in xrange( 26 ):
    adr = u64( sm.found[0].solver.eval( sm.found[0].memory.load( a + i * 8 , 8 ) , cast_to = str ) )
    s = sm.found[0].solver.eval( sm.found[0].memory.load( adr , 16 ) , cast_to = str )
    s = s[:s.index('\x00')]
    key.append( s )

print key

print ch

s = 'EBOLA'

for c in s:
    i = ch.index( c ) + 1
    y.sendlineafter( 'da:' , str( i ) )
    y.sendafter( ':' , key[ ord( ch[ i - 1 ] ) - 65 ] )


y.recvuntil( '0m' )
y.recvline()

o = open( 'flag.jpg' , 'w+' )
o.write( base64.b64decode( y.recvuntil('=') ) )
o.close()

y.interactive()
