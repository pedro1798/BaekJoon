import sys
input = sys.stdin.readline

n = int(input())
triangle = list()
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = triangle.pop()

for floor in reversed(triangle):
    temp = list()
    for j, item in enumerate(floor):
        temp.append(max(dp[j] + item, dp[j + 1] + item))
    dp = temp

print(*dp)
