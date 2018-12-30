#!/usr/bin/env python3
from __future__ import print_function
import struct
import sys
import multiprocessing as mp
import itertools as it
from hashlib import sha256
from telnetlib import Telnet


def worker(args):
    task, start = args
    hardness, task = task.split('_')
    task = task.encode('ascii')
    hardness = int(hardness)
    hardness = 2**256 / hardness
    for i in it.count(start):
        if i % 1000000 == 0: print('Progress: %d' % i)
        h = sha256(task + struct.pack('<Q', i)).digest()
        if from_bytes(h, 'big') < hardness:
            return i
    

def solve_proof_of_work(task):
    n = mp.cpu_count()
    splits = [(task, start) for start in range(0, 2 ** 64, (2 ** 64) // n)]
    pool = mp.Pool(n)
    ans = next(pool.imap_unordered(worker, splits))
    pool.terminate()
    pool.join()
    return ans


if __name__ == '__main__':
    global from_bytes
    if sys.version[0] == '2':
        input = raw_input
        def _from_bytes(n, _):
            return int(n.encode('hex'), 16)
        from_bytes = _from_bytes
    else:
        from_bytes = int.from_bytes

    r = Telnet(sys.argv[1], int(sys.argv[2]))
    for _ in range(5):
        r.read_until(b'\n')
    challenge = r.read_until(b'\n').strip().split(b' ')[1].decode('ascii')
    print('Challenge: {}'.format(challenge))
    
    sol = solve_proof_of_work(challenge)
    print('Solution: {}'.format(sol))
    r.write(str(sol).encode('ascii') + b'\n')

    r.interact()
