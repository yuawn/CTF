#!/usr/bin/env python
import angr
import re
from pwn import *

# What_You_Wanna_Be?:)_la_la

#y = process( 'RedVelvet' )

p = angr.Project( './RedVelvet' , load_options={'auto_load_libs': False} )

state = p.factory.entry_state()

sm = p.factory.simulation_manager( state , immutable = False )
#sm = proj.factory.simgr(state)

for i in xrange( 26 ):
    k = state.posix.files[0].read_from(1)
    state.solver.add( k != '\n' )
    state.solver.add( k >= ' ' )
    state.solver.add( k <= '~' )
    if i == 22:
        state.solver.add( k != 'c' )
        state.solver.add( k != 'b' )

k = state.posix.files[0].read_from(1)
state.solver.add( k == '\n' )


state.posix.files[0].seek(0)
state.posix.files[0].length = 27


good = 0x4015f2
bad = [0x401621]

sm.explore( find = good , avoid = bad )

print sm.found[0].posix.dumps(0)