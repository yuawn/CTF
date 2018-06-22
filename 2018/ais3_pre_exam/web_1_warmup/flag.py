#!/usr/bin/env python
from requests import get

# AIS3{g00d! u know how 2 check H3AD3R fie1ds.}

flag = ''

for i in xrange( 0x30 ):
    o = get( 'http://104.199.235.135:31331/index.php?p=%d' % i )
    if not len(o.headers.get( 'Partial-Flag' )): flag += ' '
    else: flag += o.headers.get( 'Partial-Flag' )


print flag