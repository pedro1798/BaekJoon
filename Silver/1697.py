import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

if n == m:
    print('0')
    sys.exit(0)

visited = [1 if i == n else 0 for i in range(100001)]

q = deque()
q.append(n)

flag = True
while flag:
    x = q.popleft()
    for i in (x - 1, x + 1, x * 2):
        if i > 100000 or i < 0:
            continue
        if not visited[i]:
            visited[i] += visited[x] + 1
            q.append(i)
            if i == m:
                print(visited[i] - 1)
                flag = False
