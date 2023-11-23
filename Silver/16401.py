import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candies = list(map(int, input().split()))

left = 1; right = max(candies)

while left <= right:
    mid = (left + right) // 2
    count = 0
    for candy in candies:
        count += (candy // mid)
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1
    
print(right)
