#!/usr/bin/env python2
import os
import re
import random
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES


key = os.urandom(16)
iv = os.urandom(16)

ori = '''
From: thor@ais3.org
To: ctfplayer@ais3.org

--BOUNDARY
Type: text
Welcome to AIS3 pre-exam.

--BOUNDARY
Type: cmd
echo 'This is the blog of oalieno'
web 'https://oalieno.github.io'
echo 'This is the blog of bamboofox team'
web 'https://bamboofox.github.io/'

--BOUNDARY
Type: text
You can find some useful tutorial on there.
And you might be wondering where is the flag?
Just hold tight, and remember that patient is virtue.

--BOUNDARY
Type: text
Here is your flag : AIS3{
'''

mod = '''
From: thor@ais3.org
To: ctfplayer@ais3.org

--BOUNDARY
Type: text
Welcome to AIS3 pre-exam.

--BOUNDARY
Type: cmd
echo 'This is the blog of oalieno'
web 'https://oalieno.github.io'
echo 'This is the blog of bamboofox team'
web 'https://bamboofox.github.io/'

--BOUNDARY
Type: text
You can find some useful tutorial on there.
And you might be wondering where is the flag?
Just hold tight, and remembe

--BOUNDARY
t ippppppppppppppppType: cmd
webtxt
Here is your fl'sheep.ga/aaaaaabbbbbbbbbbbbbbbbb}

--BOUNDARY
Type: text
Hope you like our crypto challenges.
Thanks for solving as always.
I'll catch you guys next time.
See ya!

--BOUNDARY
'''

aes = AES.new(key, AES.MODE_CBC, iv)
c = aes.encrypt(  )