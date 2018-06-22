#!/usr/bin/env python3
import os
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

from proof import proof

# some encoding problem in docker ( not important )
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('flag') as data:
    flag = data.read()

normal = '\033[0m'
bold = '\033[1m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
aquamarine = '\033[96m'

def cprint(text, color = normal):
    if color == normal:
        print(text)
    else:
        print('{}{}{}'.format(color, text, normal))

proof()

m = """
I owe you 10 bucks
- 2018/4/1 Alice
""".strip()
key = RSA.generate(2048, os.urandom)
m = int.from_bytes(m.encode('utf-8'), 'big')
s = key.sign(m, 0)[0]

cprint('◢' + '■' * 50 + '◣', bold)
cprint("- 2018/4/1", green)
cprint("Alice : Here is the receipt for the loan.", yellow)
cprint("m = {}".format(m))
cprint("Alice : Here is the digital signature (s, n, e) to prove that I actually wrote that receipt.", yellow)
cprint("s = {}".format(s))
cprint("n = {}".format(key.n))
cprint("e = {}".format(key.e))
cprint("Bob : OK, remember to pay me back someday.", aquamarine)
cprint('◥' + '■' * 50 + '◤', bold)

cprint('')
cprint("🚀  on millions years later..", red)
cprint('')

cprint('◢' + '■' * 50 + '◣', bold)
cprint("- 1002018/4/1", green)
cprint("Bob : Dormammu, I've come to bargain.", aquamarine)
cprint("Alice : Uh..., I'm not Dormammu.", yellow)
cprint("Bob: Whatever..., I think it's time for you to pay me back.", aquamarine)
cprint("Bob : Here is the receipt for the loan and also the signature.", aquamarine)

try:
    m = int(input("m = "))
    s = int(input("s = "))
    if key.verify(m, (s,)):
        m = long_to_bytes(m)
        bucks = int(m.split()[3])
        if bucks > 10:
            cprint("Alice : Oh crap, I don't have enough money..., maybe this flag can compensate you : {}".format(flag), yellow)
        else:
            cprint("Alice : Come on man, it's just 10 bucks...", yellow)
        exit(0)
    else:
        cprint("Alice : What have you done...", yellow)
except:
    exit(0)

cprint('◥' + '■' * 50 + '◤', bold)

lines = [
            [
                ("Bob : Dormammu, I've come to bargain.", aquamarine),
                ("Alice : Uh..., I'm not Dor... What is this!? Illusion?", yellow),
                ("Bob : No, it is real.", aquamarine),
                ("Alice : Good.", yellow)
            ],
            [
                ("Bob : Dormammu, I've come to bargain.", aquamarine),
                ("Alice : What is happening...", yellow),
                ("Bob : This is you gave digital signature his power from your dimension, I brought a little power from mine. This is time, endless loop time.", aquamarine),
                ("Alice : You dare!!!", bold + yellow)
            ],
            [
                ("Bob : Dormammu, I've come to bargain.", aquamarine),
                ("Alice : You can not do this forever.", yellow),
                ("Bob : Actually I can, this is how things are now. You and me trap in this moment endlessly", aquamarine),
                ("Alice : Then you would spend eternity dying", yellow),
                ("Bob : Yes, but everyone on CTF will live.", aquamarine),
                ("Alice : But you will suffer.", yellow),
                ("Bob : Pain is an old friend.", aquamarine),
                ("Alice : Ahhhhhhhhhhhh!!!", bold + yellow)
            ],
            [
                ("Bob : Dormammu, I've co...", aquamarine)
            ],
            [
                ("Bob : Dormammu, I've come to...", aquamarine),
                ("Alice : You will never win.", yellow),
                ("Bob : But I can lose again, again, again, and again forever. And make you my prisoner.", aquamarine),
                ("Alice : No. Stop. Make this stop. Set me free.", yellow)
            ],
            [
                ("Bob : No, I've come to bargain.", aquamarine),
                ("Alice : What do you want?", yellow),
                ("Bob : Take your crypto from the CTF, end your assault on my CTF, and never come back. Do it. And I will break the loop.", aquamarine),
                ("Alice : I will be back.", yellow)
            ]
        ]

for index, line in enumerate(lines):
    cprint('')
    cprint('⏳  Bob use the time stone', green)
    cprint('')
    
    cprint('◢' + '■' * 50 + '◣', bold)
    cprint("- 1002018/4/1", green)

    for l in line:
        cprint(*l)

    if index == len(lines) - 1:
        cprint("Alice left...", purple)
    else:
        cprint("Alice killed Bob...", red)

    cprint('◥' + '■' * 50 + '◤', bold)
