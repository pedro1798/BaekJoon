import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

area = list(list(input().rstrip()) for _ in range(n))
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    max_dist = 0
    
    while q:
        x, y, dist = q.popleft()
        max_dist = max(max_dist, dist)
        if not visited[x] & (1 << y):
            visited[x] |= (1 << y)
        for dir_x, dir_y in directions:
            next_x = x + dir_x; next_y = y + dir_y
            if 0 <= next_x < n and 0 <= next_y < m:
                if area[next_x][next_y] == "L" and not visited[next_x] & (1 << next_y):
                    visited[next_x] |= (1 << next_y)
                    q.append((next_x, next_y, dist + 1))
    return max_dist
    
    
result = 0
for x in range(n):
    for y in range(m):
        if area[x][y] == "L":
            visited = [0] * n
            result = max(result, bfs(x, y))
        
print(result)
