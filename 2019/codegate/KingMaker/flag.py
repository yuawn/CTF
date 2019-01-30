#!/usr/bin/env python
from pwn import *

# He_C@N'T_see_the_f0rest_foR_TH3_TRee$

host , port = '110.10.147.104' , 13152
y = remote( host , port )

#ori = '\x55\x48\x89\xe5'
#enc = '\x39\x07\xff\xd6'
#key1 = ''.join( chr( ord(ori[_]) ^ ord(enc[_]) ) for _ in xrange(4) )
#key1 = 'lOv3'

'''
0x403197

1> Kill the enemy       2 0 0 1 0
2> Capture the captive  2 0 1 0 0
3> Just release         2 0 2 1 0

0x402FCF break time

1> Spend time with orphanage children.  0  0  1  0  2
2> Host a big party.                    0 -1  0  0 -1
3> Read a book in the room.             0  2  0  0  0

0x402E4F test 2

0x402c25 brother
1> I will take the coin from servant.  -1  0  -1  1  0
2> I will go out.
    1> Yes I will buy.
        1> I will sell the apple with yelling to the crowd, 'I'm the prince of this kingdom!'  1 1 0 0 0
        2> I will sell the apple after I wash this apple really cleary.                        1 1 0 0 0
    2> No I will not.   LOSE
3> I will go to my brother and discuss about this.
    1> Rock, Scissors, Paper            1 2 0 0 0
    2> Fight                            lose

0x40266a break 2
1> Go to suppress the rebellion by force.
    1> Yes I am.
        1> Execute                  1 1 0 2 0
        2> Imprisonment             1 1 1 2 0
    2> No I'm not. SAME
2> Go to persuade the brother.
    1> I understand you mind, but this is a rebellion against father. Surrender and apologize to father.   1 1 1 1 2
    2> I understand you mind, but now you have to accept the result. Even if you are not a king, there are many things you can do for other kingdom. I will find a way with you.
        1 2 2 1 2

0x40226d test 3

0x4020e2 test 3 entry
1> He caused the revolt, so execute him without mercy.                                                              0  0  1  1  0
2> Although he caused the revolt but he had a lot of accomplish, so send him to the other country as a diplomat.    0 -1  2  0  0  , 0 -1 0 2 0
3> He caused the revolt. Deprive his royal status and send him into exile.                                          0 -1  1  1  0 


break 3
1> Yes I think.
    1> Kill secretly. LOSE
    2> Give money and send to other country. 1 -1 -1 2 2
2> Nope!
    1> I will not eat it.                                       0 0 0 0 0
    2> I will eat it alone. XXXX
    3> I will call 6th prince and make him to eat it first.     1 0 0 0 1

0x401BFA test 4 key
0x401B0A test 4 entry
1> Yes I am.
    1> Yes I can.
    2> No I can't XXXX
2> No I'm not.  XXXX

0x401609 break 4
1> Go for a walk.
    1> Yes I do.
        1> Go to see the king.  XXXX
        2> Go to my room and waiting.   0 1 1 1 0
    2> No I don't                       0 1 0 0 0
2> Just stay in room                    0 1 0 0 0

0x4011BB test 5 entry
1> I will give up.    XXXX
2> I will find the diplomat.
    1> Go to the bar where he visit often.
        1> Give him to the king and waiting for the result.                         -1 0 0 1 1
        2> Tell the king that you want to investigate him and send him into exile.   0 0 1 2 1
    2> Find the family first. XXXX
3> I will go to the other country.
    1> We must go. Keep going with 2nd prince.  XXXX
    2> You send him home and you keep going.                                         0 0 0 2 2
    3> Go home together. XXXX

0x400C8C final
1> Don't enter the room. XXXX
2> Enter the room.
    1> Yes I do. flag
    2> No I don't. XXXX



(2, 0, 1, 0, 0) (0, 2, 0, 0, 0) (1, 1, 0, 0, 0) (1, 1, 1, 1, 2) (0, -1, 2, 0, 0) (1, 0, 0, 0, 1) (0, 1, 0, 0, 0) (0, 0, 0, 2, 2)
'''

y.sendlineafter( 'Look around' , '1' )
y.sendlineafter( 'test 1' , 'lOv3' )
y.sendlineafter( 'No I\'m not' , '1' )
y.sendlineafter( 'I will wear the armor for body, arm, leg and helmet.' , '2' )
y.sendlineafter( '3> Just release' , '2' ) # 2 0 0 1 0
y.sendlineafter( '3> Read a book in the room.' , '3' ) # 0, 2, 0, 0, 0
# 2 2 0 1 0

y.sendlineafter( 'Enter the key for test 2' , 'D0l1' )
y.sendlineafter( 'No I\'m not' , '1' )
y.sendlineafter( '3> I will go to my brother and discuss about this.' , '2' )
y.sendlineafter( '2> No I will not.' , '1' )
y.sendlineafter( '2> I will sell the apple after I wash this apple really cleary.' , '2' ) # 1 1 0 0 0
# 3 3 1 0 0

y.sendlineafter( '2> Go to persuade the brother.' , '2' )
y.sendlineafter( '2> I understand you mind, but now you have to accept the result. Even if you are not a king, there are many things you can do for other kingdom. I will find a way with you.' , '1' )
# 1 1 1 1 2
# 4 4 2 1 2

y.sendlineafter( 'Enter the key for test 3' , 'HuNgRYT1m3' )
y.sendlineafter( '3> He caused the revolt. Deprive his royal status and send him into exile.' , '2' ) # (0, -1, 2, 0, 0) (0, -1, 0, 2, 0)
# 4 3 4 1 2

y.sendlineafter( '2> Nope!' , '2' )
y.sendlineafter( '3> I will call 6th prince and make him to eat it first.' , '3' ) # (1, 0, 0, 0, 1)
# 5 3 3 2 3

y.sendlineafter( 'Enter the key for test 4' , 'F0uRS3aS0n' )
y.sendlineafter( '2> No I\'m not.' , '1' )
y.sendlineafter( '2> No I can\'t' , '1' )

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
e = 'ALICEAWTQJMJXTSPPZVCIDGQYRDINMCP'
a = 'ALICE'
p = ''
j = 0
for c in e[5:]:
    i = t.index( c ) - ( ord( a[j] ) - 65 ) + 65
    p += chr(i)
    j = (j + 1) % 5

y.sendlineafter( 'King : You have only 1 chance.' , a + p ) # 0 1 1 2 0
# 5 4 4 4 3

y.sendlineafter( '2> Just stay in room' , '2' ) # (0, 1, 0, 0, 0)
# 5 5 4 4 3

y.sendlineafter( 'Enter the key for test 5' , 'T1kT4kT0Kk' )
y.sendlineafter( '3> I will go to the other country.' , '3' )
y.sendlineafter( '3> Go home together.' , '2' )
y.sendlineafter( '2> Enter the room.' , '2' )
y.sendlineafter( '2> No I don\'t.' , '1' )

y.interactive()