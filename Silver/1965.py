import sys
input = sys.stdin.readline

def bs(l, r, targ):
    while l < r:
        m = (l + r) // 2
        if dp[m] < targ:
            l = m + 1
        else:
            r = m
    return r

def solution(n, arr, dp):
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bs(0, len(dp) - 1, arr[i])] = arr[i]
            
    print(len(dp))
    
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]
    solution(n, arr, dp)
