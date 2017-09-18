#!/usr/bin/env python
# -*- coding: ascii -*-

# Bugs_Bunny{Baby_RSA_Its_Cool_Lik3_school_haHAha}

'''
http://factordb.com/index.php?query=20473673450356553867543177537

rsatool -p  2165121523231 -q 9456131321351327 -e 17

n = 20473673450356553867543177537 (0x42276cfdae8860a5939be941)

e = 17 (0x11)

d = 12043337323733585630059001753 (0x26ea03e084b4ed299acb7799)

p = 2165121523231 (0x1f81b4c9e1f)

q = 9456131321351327 (0x21984d245bcc9f)
'''
n = 20473673450356553867543177537
d = 12043337323733585630059001753


enc = open( 'enc.txt' , 'r' )
flag = ''

for i in enc.read().split('\n')[:-1]:
    flag += chr( pow( int( i ) , d , n ) )

print flag