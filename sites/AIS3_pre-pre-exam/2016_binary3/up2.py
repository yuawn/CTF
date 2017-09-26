import angr

avoid = (0x401d46, 0x401d86, 0x401dd1)
good = 0x402471

proj = angr.Project('binary3')

state = proj.factory.full_init_state(args=['./binary3'])

# stdin
state.posix.files[0].seek(0)
state.posix.files[0].length = 30

path_group = proj.factory.path_group(state)
path_group.explore(find=good, avoid=avoid)

print path_group.found
print path_group.found[0].state.posix.dumps(0)