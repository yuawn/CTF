#!/usr/bin/env python3
from sys import exit

# PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}

'''
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f5008e579e8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/guessme/can-you-guess-me.py', '__cached__': None, 'exit': <built-in function exit>, 'secret_value_for_password': 'not even a number; this is a damn string; and it has all 26 characters of the alphabet; abcdefghijklmnopqrstuvwxyz; lol', 'flag': 'PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}', 'exec': <function exec at 0x7f5008da0158>, 'val': 0, 'inp': 'print(vars())', 'count_digits': 10}
'''

# print(vars())

flag = 'pctf{aaaaaa}'

secret = 666

'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'count_digits', 'exec', 'exit', 'flag', 'inp', 'secret_value_for_password', 'val']
'''


while True:
    inp = input("Input value: ")
    print( set( inp ) )
    print( len( set( inp ) ) )

    try:
        val = eval( inp )
        if val == secret:
            print( 'Success!' )

    except:
        print( 'raise' )