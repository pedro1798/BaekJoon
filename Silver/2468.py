import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
area = list(list(map(int, input().split())) for _ in range(n))
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
max_height = max(max(row) for row in area)

def bfs(height: int, visited: list, i: int, j: int):
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        visited[i] |= (1 << j)
        for x, y in directions:
            nx = i + x; ny = j + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx] & (1 << ny) and area[i][j] > height:
                    visited[nx] |= (1 << ny)
                    q.append((nx, ny))

def find_safe_area(height: int):
    visited = [0] * n
    num_of_safe_area = 0
    for i in range(n):
        for j in range(n):
            if not visited[i] & (1 << j) and area[i][j] > height:
                bfs(height, visited, i, j)  # update visited
                num_of_safe_area += 1
    return num_of_safe_area
    
result = list(find_safe_area(height) for height in range(1, max_height))
print(max(result) if result else 1)    
