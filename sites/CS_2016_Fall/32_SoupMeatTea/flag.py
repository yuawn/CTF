import angr
from pwn import *

host = 'csie.ctf.tw'
port = 10133
#y = remote(host,port)

ag = angr.Project('c',load_options={'auto_load_libs': False})

pa = ag.factory.path_group().explore(find=0x40067e)

res = pa.found[0].state.posix.dumps(0)

log.success(res)

#y.send(res)

#print y.recvall()
