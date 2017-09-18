from pwn import *
import angr
#FLAG{C4lcuL4t0r?_2_Sl0w_4_Me}

host = '127.0.0.1'
port = 4000
y = remote(host,port)

ag = angr.Project('serial',load_options={'auto_load_libs':False})

pa = ag.factory.path_group().explore(find=0x400827)

res = pa.found[0].state.posix.dumps(0)

log.success(res)

y.send(res)

print y.recvall()
