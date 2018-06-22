#!/usr/bin/env python3
import os
import re
import random
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from urllib.parse import quote
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

flag = 'yuawnnnnnnnnn'


# simplify mail format
mail_for_ctfplayer = '''
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
Here is your flag : {}

--BOUNDARY
Type: text
Hope you like our crypto challenges.
Thanks for solving as always.
I'll catch you guys next time.
See ya!

--BOUNDARY
'''.format(flag).lstrip().encode('utf-8')

mod = '''From: thor@ais3.org
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
Just hold tight, and remember

--BOUNDARY
 is virtue.

--BOUNType: cmd
webxt
Here is your fla'60.251.236.16/
'''.lstrip().encode('utf-8')


quotes = ['Keep on going never give up.',
          'Believe in yourself.',
          'Never say die.',
          "Don't give up and don't give in.",
          'Quitters never win and winners never quit.']

seen = False
key = b'\xa4\xcf\x03C0\x7f%\xaf\x13\xf6\xe3s;\xb64\xb5'
iv = b'\xd4\xe2I\x85\xe8l\xe0O`\x04IQ\xa1-\x10-'

def pad(text):
    L = -len(text) % 16
    return text + bytes([L]) * L

def unpad(text):
    L = text[-1]
    if L > 16:
        raise ValueError
    for i in range(1, L + 1):
        if text[-i] != L:
            raise ValueError
    return text[:-L]

def parse_mail(mail):
    raw_mail = b""

    # parse many chunk
    while True:

        # throw away the delimeter
        _, _, mail = mail.partition(b'--BOUNDARY\n')
        #print( mail )
        if not mail:
            break

        # parse Type
        type_, _, mail = mail.partition(b'\n')
        print(mail)
        type_ = type_.split(b': ')[1]

        # Type: text
        if type_ == b'text':
            text, _, mail = mail.partition(b'\n\n')
            raw_mail += text + b'\n'

        # Type: cmd
        elif type_ == b'cmd':

            # parse many cmd
            while True:

                # see '\n\n' then continue to next chunk
                if mail[:1] == b'\n':
                    mail = mail[1:]
                    break
                
                # parse cmd, content
                cmd, _, mail = mail.partition(b"'")
                content, _, mail = mail.partition(b"'\n")

                # echo 'content' ( print some text )
                if cmd.startswith(b'echo'):
                    raw_mail += content + b'\n'

                # web 'content' ( preview some of the text on webpage )
                elif cmd.startswith(b'web'):
                    x = content.find(b'//')
                    if x != -1:
                        url = content[:x].decode('utf-8') + '//' + quote(content[x+2:])
                    else:
                        url = 'http://' + quote(content)
                    try:
                        #print( '-------' )
                        #url = 'http://60.251.236.17'
                        print( url )
                        req = urlopen(url)
                        text = req.read()
                        #print( 'text -> ' , text )
                        #print( '-------' )
                        raw_mail += b'+ ' + content + b'\n'
                        raw_mail += b'\n'.join(re.findall(b'<p>(.*)</p>', text)) + b'\n'
                    except (HTTPError, URLError) as e:
                        pass
    return raw_mail

def read_mail(mail):
    #print( mail )
    # I am so busy right now, no time to read the mails
    pass

def getmail():
    global seen
    if not seen:
        aes = AES.new(key, AES.MODE_CBC, iv)
        mail = aes.encrypt(pad(mail_for_ctfplayer))
        #print(b64encode(mail).decode('utf-8'))
        seen = True
        return b64encode(mail).decode('utf-8')
    else:
        print('you have read all mails.')

def sendmail(mail):
    mail = b64decode(mail)
    print( len(mail) )
    aes = AES.new(key, AES.MODE_CBC, iv)
    mail = unpad(aes.decrypt(mail))
    #print( '------------' )
    #print( 'raw ->' , mail )
    #print( '------------' )
    mail = parse_mail(mail)
    read_mail(mail)

def menu():
    print('')
    print('{:=^20}'.format(' menu '))
    print('1) ctf player mailbox')
    print('2) send me a mail')
    print('3) quit')
    print('=' * 20)

    option = int(input('> ').strip())
    if option == 1:
        getmail()
    elif option == 2:
        mail = input('mail : ')
        sendmail(mail)
    elif option == 3:
        print(random.choice(quotes))
    else:
        exit(0)


'''
mm = getmail()

m = b64decode(mm)
#print( m )
m = b'\xf8' + m[1:]

sendmail( b64encode( mod ) )
'''
parse_mail( mod )

