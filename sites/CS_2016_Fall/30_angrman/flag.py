import angr
from pwn import *
#FLAG{Smartest_Angrman_Online}

y = process('amgrman')

ag = angr.Project('angrman',load_options={'auto_load_libs': False})

pa = ag.factory.path_group().explore(find=0x400d2b)

res = pa.found[0].state.posix.dumps(0)

y.send(res)

print y.recvall()

print res
