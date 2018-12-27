#!/usr/bin/env python3
import angr
import claripy

proj = angr.Project('angrme')
simgr = proj.factory.simgr()
simgr.explore(find=lambda s: b":)" in s.posix.dumps(1))
s = simgr.found[0]
print(s.posix.dumps(0))