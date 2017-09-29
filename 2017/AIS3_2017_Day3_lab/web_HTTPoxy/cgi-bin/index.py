#!/usr/bin/env python
#
# By Orange Tsai :P
#

import os
import cgi
import sqlite3
import requests
from urllib import quote
from base64 import b64encode

print "Content-Type: text/html\n"

query  = os.environ["QUERY_STRING"]
params = dict(cgi.parse_qsl(query))

WAF = 'http://127.0.0.1/waf/'

def check_param(s):
    data = {
        'data': s
    }
    r = requests.post(WAF, data)
    content = r.content.strip()
    if r.content == 'ok':
        return True
    else:
        return False



news_id = params.get('id', '1')
if not check_param(news_id):
	news_id = '1'

conn = sqlite3.connect('/var/www/db/flag.db')
cur = conn.cursor()
cur.execute("SELECT * FROM news WHERE id='%s'" % news_id)
data = cur.fetchone()
if data:
	print data[1]
else:
	print 'Hacker?'

