#!/usr/bin/env python2
import angr , claripy

#

avoid = (0x401820 , 0x403b4a , 0x400c51 , 0x403b4c)
#good = (0x403aea , 0x403b50)
good = 0x400c40
goodi = 0x403aea
goodag = 0x403b50

ag = angr.Project('./rev400',load_options={'auto_load_libs':False})

state = ag.factory.blank_state(addr = 0x400c10)

flag = claripy.BVS('flag_buf' , 8 * 12)

state.memory.store( 0xd0000000 , './rev400' )
state.memory.store( 0xd0000008 , flag )

state.stack_push( 0xd0000008 )
state.stack_push( 0xd0000000 )

state.regs.rdi = 2
state.regs.rsi = state.regs.rsp

state.add_constraints( flag.get_byte(0) > 31 )
state.add_constraints( flag.get_byte(0) < 126  )
state.add_constraints( flag.get_byte(1) > 31 )
state.add_constraints( flag.get_byte(1) < 126 )
state.add_constraints( flag.get_byte(2) > 31 )
state.add_constraints( flag.get_byte(2) < 126 )
state.add_constraints( flag.get_byte(3) > 31 )
state.add_constraints( flag.get_byte(3) < 126 )
state.add_constraints( flag.get_byte(4) > 31 )
state.add_constraints( flag.get_byte(4) < 126 )
state.add_constraints( flag.get_byte(5) > 31 )
state.add_constraints( flag.get_byte(5) < 126 )
state.add_constraints( flag.get_byte(6) > 31 )
state.add_constraints( flag.get_byte(6) < 126 )
state.add_constraints( flag.get_byte(7) > 31 )
state.add_constraints( flag.get_byte(7) < 126 )
state.add_constraints( flag.get_byte(8) > 31 )
state.add_constraints( flag.get_byte(8) < 126 )
state.add_constraints( flag.get_byte(9) > 31 )
state.add_constraints( flag.get_byte(9) < 126 )
state.add_constraints( flag.get_byte(10) > 31 )
state.add_constraints( flag.get_byte(10) < 126 )
state.add_constraints( flag.get_byte(11) > 31 )
state.add_constraints( flag.get_byte(11) < 126 )
state.add_constraints( flag.get_byte(12) > 31 )
state.add_constraints( flag.get_byte(12) < 126 )
state.add_constraints( flag.get_byte(13) > 31 )
state.add_constraints( flag.get_byte(13) < 126 )
state.add_constraints( flag.get_byte(14) > 31 )
state.add_constraints( flag.get_byte(14) < 126 )
state.add_constraints( flag.get_byte(15) > 31 )
state.add_constraints( flag.get_byte(15) < 126 )
state.add_constraints( flag.get_byte(16) > 31 )
state.add_constraints( flag.get_byte(16) < 126 )

print 'Start!'

pg = ag.factory.path_group( state ).explore(find = good , avoid = avoid)

print pg.found[0]
print pg.found[0].state.posix.dumps(0)
print pg.found[0].state.se.any_n_str( flag , 1 )