import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = n * m
a, b, c, d, e = map(int, input().split())
print(f"{a - num} {b - num} {c - num} {d - num} {e - num}")
