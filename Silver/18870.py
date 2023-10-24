from sys import stdin as ss
from sys import stdout as sw

n = int(ss.readline())
input = list(map(int, ss.readline().split()))
sorted_input = sorted(list(set(input)))


def b_search(target, l, r):
    r -= 1
    while l < r:
        m = (l + r) // 2
        if target == sorted_input[m]:
            return m
        elif target > sorted_input[m]:
            l = m + 1
        else:
            r = m - 1
    return l

for i in input:
    print(b_search(i, 0, len(sorted_input)), end = " ")
