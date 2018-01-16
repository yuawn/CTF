#!/usr/bin/env python
from pwn import *


a = ( 0x5555555555555555 + 1 )
b = ( ( a * 3 ) << 4 ) & 0xffffffffffffffff

print hex( b )