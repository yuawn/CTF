#!/usr/bin/python2

from pwn import *
import base64
import sys

# register to obtain the cypher1
conn = remote ('csie.ctf.tw', 10127)
conn.recvuntil ('--------------------')
conn.recvuntil ('[0] Register')
conn.recvuntil ('[1] Login')
conn.recvuntil ('--------------------')
conn.send ('0\n')
conn.recvuntil ('Your user name: ')
conn.send ('1234\n')
conn.recvuntil ('Your password: ')
conn.send ('1234567\n')
conn.recvuntil ('[+] Your token: ')
cypher1 = conn.recvline ()
conn.close ()

# register to obtain the cypher2
conn = remote ('csie.ctf.tw', 10127)
conn.recvuntil ('--------------------')
conn.recvuntil ('[0] Register')
conn.recvuntil ('[1] Login')
conn.recvuntil ('--------------------')
conn.send ('0\n')
conn.recvuntil ('Your user name: ')
conn.send ('1234567890admin\n')
conn.recvuntil ('Your password: ')
conn.send ('123456789012\n')
conn.recvuntil ('[+] Your token: ')
cypher2 = conn.recvline ()
conn.close ()

# use cypher1 and cypher2 to create the admin cypher
admincypher = base64.b64encode (base64.b64decode (cypher1)[:16] + base64.b64decode (cypher2)[16:])

# use the admin cypher to get the flag
conn = remote ('csie.ctf.tw', 10127)
conn.recvuntil ('--------------------')
conn.recvuntil ('[0] Register')
conn.recvuntil ('[1] Login')
conn.recvuntil ('--------------------')
conn.send ('1\n')
conn.recvuntil ('Provide your token: ')
conn.send (admincypher + '\n')
conn.recvuntil ('Provide your username: ')
conn.send ('1234\n')
conn.recvuntil ('Provide your password: ')
conn.send ('123456789012\n')
conn.recvuntil ('Hi admin: ')
flag = conn.recvline ()
conn.close ()

print ('Here is the flag:')
print (flag)
