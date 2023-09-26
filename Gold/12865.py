from sys import stdin as ss

n, k = map(int, ss.readline().split())
items = [[0,0]]

for _ in range(n):
	items.append(list(map(int, ss.readline().split())))

dp = [[0] * (k+1) for _ in range(n+1)] #value 

def knapSack():
	for i in range(1, n+1):
		for j in range(k+1): 
			v = items[i][1]
			
			if items[i][0] > j: 
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max(dp[i-1][j], v + dp[i-1][j - items[i][0]])
				
	print(dp[-1][-1])

knapSack()