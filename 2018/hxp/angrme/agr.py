#!/usr/bin/env python3
import angr
import claripy

p = angr.Project( './angrme' )

base = 0x400000

#flag_chars = [ claripy.BVS( 'flag_%d' % i , 8 ) for i in range( 0x24 ) ]
#flag = claripy.Concat( *flag_chars + [ claripy.BVV( b'\n' ) ] )

#state = p.factory.entry_state( stdin = flag )
#sm = p.factory.simulation_manager( state )

sm = p.factory.simgr()

good = base+0x2370
bad = base+0x2390
sm.explore( find = good , avoid = bad )

print( sm.found[0].posix.dumps(0) )