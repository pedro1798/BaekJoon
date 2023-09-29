from sys import stdin as ss

n, k = map(int, ss.readline().split())
coin = [int(ss.readline()) for _ in range(n)]

dp = [1] + [0 for i in range(k)]

for i in coin:
	for j in range(i, k+1):
		if j-i >= 0:
			dp[j] += dp[j-i]
print(dp[-1])


