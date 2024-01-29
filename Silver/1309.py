n = int(input())

dp = [3, 7]

if n < 3:
    print(dp[n-1])
else:
    for i in range(2, n):
        dp.append((dp[i-2] * 3 + (dp[i-1] - dp[i-2]) * 2) % 9901)
    print(dp[-1])