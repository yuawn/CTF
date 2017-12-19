# HW6
## break
* angr.
* General way of angr.
* From avoid[] list get some input.
* Set constrians of input to continue.
```python=
#!/usr/bin/env python
import angr

# CTF{PinADXAnInterfaceforCustomizableDebuggingwithDynamicInstrumentation}

p = angr.Project( './break' )

state = p.factory.entry_state()
#state = p.factory.full_init_state( args = ['./break'] )

g = range( 32 )

s = 'CTF{PinADXAnInterfaceforCustomizableDebuggingwithDynamicIns'

for c in s:
    k = state.posix.files[0].read_from(1)
    state.solver.add( k == c )

k = state.posix.files[0].read_from(1)
state.solver.add( k != 10 )

state.posix.files[0].seek(0)
state.posix.files[0].length = 89

sm = p.factory.simulation_manager( state )

gg = [ 0x400831 , 0x4008ff ]

sm.explore( find = 0x40091f , avoid = gg  )

print sm.found[0].posix.dumps(0)
```