import angr

avoid = (0x401d46, 0x401d86, 0x401dd1)
good = 0x402471

ag = angr.Project('binary3',load_options={'auto_load_libs': False})


pa = ag.factory.path_group().explore(find=good, avoid=avoid)


res = pa.found[0].state.posix.dumps(0)

print pa.found
print ''.join( hex(ord(c)).replace('0x','\\x') for c in res )