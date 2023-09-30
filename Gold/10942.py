from sys import stdin as ss

n = int(ss.readline())
input = list(map(int, ss.readline().split()))
m = int(ss.readline())
rng = [list(map(int, ss.readline().split())) for _ in range(m)]

dp = [[0] * n for _ in range(n)]

def is_palindrome(n):
	for i in range(n):
		dp[i][i] = 1
	
	for i in range(n-1):
		if input[i] == input[i+1]:
			dp[i][i+1] = 1
		
	for length in range(3, n+1):
		for i in range(n - length + 1):
			j = i + length - 1
			if input[i] == input[j] and dp[i+1][j-1]:
				dp[i][j] = 1			
					
is_palindrome(n)
for i in range(m):
	print(dp[rng[i][0]-1][rng[i][1]-1])
