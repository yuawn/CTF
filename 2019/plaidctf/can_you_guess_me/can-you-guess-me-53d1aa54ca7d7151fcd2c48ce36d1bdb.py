#! /usr/bin/env python3

from sys import exit
from secret import secret_value_for_password, flag, exec

print(r"")
print(r"")
print(r"  ____         __   __           ____                     __  __       ")
print(r" / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___  ")
print(r"| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \ ")
print(r"| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/ ")
print(r" \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___| ")
print(r"                                                                       ")
print(r"")
print(r"")

try:
    val = 0
    inp = input("Input value: ")
    count_digits = len(set(inp))
    if count_digits <= 10:          # Make sure it is a number
        val = eval(inp)
    else:
        raise

    if val == secret_value_for_password:
        print(flag)
    else:
        print("Nope. Better luck next time.")
except:
    print("Nope. No hacking.")
    exit(1)
