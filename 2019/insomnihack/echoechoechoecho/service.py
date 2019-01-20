#!/usr/bin/env python3

from os import close
from random import choice
import re
from signal import alarm
from subprocess import check_output
from termcolor import colored

alarm(10)

colors = ["red","blue","green","yellow","magenta","cyan","white"]
# thanks http://patorjk.com/software/taag/#p=display&h=0&f=Crazy&t=echo
banner = """
                            _..._                 .-'''-.
                         .-'_..._''.             '   _    \\
       __.....__       .' .'      '.\  .       /   /` '.   \\
   .-''         '.    / .'           .'|      .   |     \  '
  /     .-''"'-.  `. . '            <  |      |   '      |  '
 /     /________\   \| |             | |      \    \     / /
 |                  || |             | | .'''-.`.   ` ..' /
 \    .-------------'. '             | |/.'''. \  '-...-'`
  \    '-.____...---. \ '.          .|  /    | |
   `.             .'   '. `._____.-'/| |     | |
     `''-...... -'       `-.______ / | |     | |
                                  `  | '.    | '.
                                     '---'   '---'
"""

def bye(s=""):
    print(s)
    print("bye")
    exit()

def check_input(payload):
    if payload == 'thisfile':
        bye(open("/bin/shell").read())

    if not all(ord(c) < 128 for c in payload):
        bye("ERROR ascii only pls")

    if re.search(r'[^();+$\\= \']', payload.replace("echo", "")):
        bye("ERROR invalid characters")

    # real echolords probably wont need more special characters than this
    if payload.count("+") > 1 or \
            payload.count("'") > 1 or \
            payload.count(")") > 1 or \
            payload.count("(") > 1 or \
            payload.count("=") > 2 or \
            payload.count(";") > 3 or \
            payload.count(" ") > 30:
        bye("ERROR Too many special chars.")

    return payload


print(colored(banner, choice(colors)))
print("Hi, what would you like to echo today? (make sure to try 'thisfile')")
payload = check_input(input())


print("And how often would you like me to echo that?")
count = max(min(int(input()), 10), 0)

payload += "|bash"*count

close(0)
result = check_output(payload, shell=True, executable="/bin/bash")
bye(result.decode())