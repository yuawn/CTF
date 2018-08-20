#!/usr/bin/env python
from pwn import *


y = remote( '10.13.37.3' , 1771 )

y.sendlineafter( ']: ' , '1' )

o = open( './propaganda' , 'w+' )

o.write( y.recvall() )
o.close()


y.interactive()