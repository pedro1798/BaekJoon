import itertools
from sys import stdin as ss

n, r = map(int, ss.readline().split())
arr = [i for i in range(1, n + 1)]
nCr = itertools.combinations(arr, r)
for i in list(nCr):
    print(*i)
