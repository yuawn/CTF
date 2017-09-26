#!/usr/bin/env python2
import angr , claripy

#ais3{readING_ASSemblY_4_FUN!}

avoid = (0x4006c8 , 0x40063c)
good = 0x4006bc

ag = angr.Project('./bin1',load_options={'auto_load_libs':False})

state = ag.factory.blank_state(addr = 0x40066b)

flag = claripy.BVS('flag_buf' , 8 * 0x1d) 

state.memory.store( 0xf0000000 , './bin1' )
state.memory.store( 0xf0000008 , flag )

state.stack_push( 0xf0000008 )
state.stack_push( 0xf0000000 )

state.regs.rdi = 2
state.regs.rsi = state.regs.rsp

state.add_constraints( flag.get_byte(0) == ord( 'a' ) )
state.add_constraints( flag.get_byte(1) == ord('i'))
state.add_constraints( flag.get_byte(2) == ord('s'))
state.add_constraints( flag.get_byte(3) == ord('3'))
state.add_constraints( flag.get_byte(4) == ord('{'))



pg = ag.factory.path_group( state ).explore(find = good , avoid = avoid)

print pg.found[0]
print pg.found[0].state.posix.dumps(0)
print pg.found[0].state.se.any_n_str( flag , 1 )