import sys
from itertools import combinations
#from math import factorial
input = sys.stdin.readline

n, m = map(int, input().split())
towns = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    towns[a] |= (1 << b)

count = 0
for i, j in combinations(range(1, n + 1), 2):
    to_billage = towns[i] & towns[j]  # 비트 and로 교집합 구하기
    n = bin(to_billage).count("1")
    count += n * (n - 1) // 2  # nC2

print(count)
