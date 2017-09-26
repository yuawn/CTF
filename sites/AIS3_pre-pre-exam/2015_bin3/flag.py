import angr

#AIS3{dementia}

avoid = (0x4001df)
good = 0x400231

ag = angr.Project('bin3',load_options={'auto_load_libs': False})

initial_state = ag.factory.entry_state(args=[ag.filename], add_options={'BYPASS_UNSUPPORTED_SYSCALL'})

pa = ag.factory.path_group(initial_state).explore(find = good , avoid = avoid)
#ex = ag.surveyors.Explorer(find=good, avoid=avoid)
#ex.run()
#print ex.found[0]


res = pa.found[0].state.posix.dumps(0)

print pa.found
print res