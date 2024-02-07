import sys

input = sys.stdin.readline

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n < len(dp):
            print(dp[n - 1])
        else:
            while len(dp) < n:
                dp.append(dp[-1] + dp[-5])
            print(dp[-1])

if True:
    solution()
