import time
import angr
import claripy

avoid = (0x406c8, 0x40063c)
good = 0x4006bc
main = 0x40066b

start_t = time.time()

proj = angr.Project('bin1')

argv=['./bin1', claripy.BVS('flag', 8*30)]
state = proj.factory.blank_state(addr=main)

# Prepare the argc and argv
state.memory.store(0xd0000000, argv[0]) # content of argv[0], which is the executable name
state.memory.store(0xd0000020, argv[1]) # content of argv[1], which is our flag

state.stack_push(0xd0000020)
state.stack_push(0xd0000000)

state.regs.rdi = 2 # argc
state.regs.rsi = state.regs.rsp # argv

state.add_constraints(argv[1].get_byte(0) == ord('a'))
state.add_constraints(argv[1].get_byte(1) == ord('i'))
state.add_constraints(argv[1].get_byte(2) == ord('s'))
state.add_constraints(argv[1].get_byte(3) == ord('3'))
state.add_constraints(argv[1].get_byte(4) == ord('{'))
state.add_constraints(argv[1].get_byte(28) == ord('}'))
state.add_constraints(argv[1].get_byte(29) == 0)

path_group = proj.factory.path_group(state, threads=4)

print 'start explore'
path_group.explore(find=good, avoid=avoid)

print path_group.found
print path_group.found[0].state.se.any_n_str(argv[1], 1)

stop_t = time.time()
print 'Used ... ' + str(stop_t - start_t)