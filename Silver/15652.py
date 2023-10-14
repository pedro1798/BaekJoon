import itertools
from sys import stdin as ss

n, r = map(int, ss.readline().split())
arr = [i for i in range(1, n + 1)]
nHr = itertools.combinations_with_replacement(arr, r)  # iterable에서 원소 개수가 r개인 중복 조합 뽑기
for i in list(nHr):
    print(*i)
