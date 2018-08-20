#!/usr/bin/env python
from pwn import *

host = '10.13.37.3'
port 7777

y = remote( host , port )


y.interactive()
