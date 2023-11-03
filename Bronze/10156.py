import sys
input = sys.stdin.readline
# 과자 가격, 살 과자 개수, 가진 돈
k, n, m = map(int, input().split())
d = k* n - m
print(d if d >= 0 else 0)
