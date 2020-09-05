#!/usr/bin/env python
import hashlib
from pwn import *


for i in range( 0x1000000 ):
    key = str(i).ljust(0x40,'a')
    if hashlib.md5( key ).hexdigest()[:2] == '27':
        print key
        print hashlib.md5( key ).hexdigest()
        break