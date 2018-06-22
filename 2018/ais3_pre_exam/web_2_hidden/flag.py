#!/usr/bin/env python
from requests import post
from IPython import embed
import re


URL = 'http://104.199.235.135:31332/_hidden_flag_.php'
flag = ''

o = post( URL , { 'c':1,'s':'6d16a8d466b16f456bf9a3faeef31db59612cbb11ce64e0196b07d25ed2cff4e' } )

for i in xrange( 2 , 100000 ):
    o = post( URL , { 'c':re.findall( '.*value="(.*)".*' , o.text )[0],'s':re.findall( '.*value="(.*)".*' , o.text )[1] } )
    if not i % 500:
        print i
    if 'got' in o.text:
        print o.text
        embed()

