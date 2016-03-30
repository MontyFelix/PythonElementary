import math
from multiprocessing import Pool
from contextlib import closing
import cProfile
import time


def fa(a):
    t = time.time()
    q = math.factorial(a)
    s = time.time()
    return q


if __name__ == '__main__':
    w = time.time()
    with closing(Pool(processes=3)) as p:
        results = p.map(fa, range(1, 75), chunksize=10)
        p.terminate()
    e = time.time()
    print results, e-w
