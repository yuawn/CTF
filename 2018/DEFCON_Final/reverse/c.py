#!/usr/bin/env python

import editdistance
from pwn import *

context.arch = 'amd64'

r = process(['./reverse', '10.13.37.3', '--numpad'])

r.sendline('1')

sleep(1)

while True:
    data = r.recvuntil('????')
    data = data.split('\n')[-1]
    data = data.split(' ')[-1]
    data = data.split('\x1b[8;33H\x1b[33m')
    opcode = data[0].split('\x1b')
    critical( opcode )
    opcode = opcode[0]
    # log.info('opcode: ' + repr(opcode))

    r.recvuntil('(1)')
    data = r.recv().split(';21H')
    choose = []
    for i in range(5):
        if i == 0:
            d = data[i][1:]
            choose.append(d.split('\x1b')[0])
        else:
            d = data[i][4:]
            choose.append(d.split('\x1b')[0])

    print ''
    print ''

    p = 0

    try:
        opcode = disasm(opcode.decode('hex'), byte=0, offset=0).replace('ffffffff', '')
    except:
        succes( opcode )
        opcode = raw_input( '>>>>>>>' )
        edit_distance = []
        for i in range(5):
            edit_distance.append(editdistance.eval(opcode, choose[i]))
            print i+1, choose[i]

        print edit_distance

        select = edit_distance.index(min(edit_distance)) + 1
        print select
        r.sendline(str(select))
        continue
        

    log.info('opcode: ' + opcode)

    edit_distance = []
    for i in range(5):
        edit_distance.append(editdistance.eval(opcode, choose[i]))
        print i+1, choose[i]

    print edit_distance

    select = edit_distance.index(min(edit_distance)) + 1
    print select
    r.sendline(str(select))

# r.interactive()