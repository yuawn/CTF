#!/usr/bin/env python
from pwn import *
import os , codecs , json , subprocess


y = remote( '180.163.241.53' , 10001 )

y.recvuntil( 'pow.py)' )

cmd = y.recvline()
print cmd
o = subprocess.check_output( 'python3 pow.py %s' % cmd , shell=True )
print o
y.sendline( o )


print y.recvuntil( '53)' )
'''
y.sendlineafter( '> ' , '1.2.3.4:53' )


logs = eval( open( 'info' ).read() )
for i in logs:
    print i

password = ''
y.sendlineafter( '> ' , password )
'''

y.interactive()
