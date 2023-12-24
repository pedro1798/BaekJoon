import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, visited, color):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and painting[nx][ny] in color:
                visited[nx][ny] = 1
                q.append((nx, ny))
    
if __name__ == "__main__":
    n = int(input())
    painting = [list(input().rstrip()) for _ in range(n)]
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    visited = [[0] * n for _ in range(n)]
    normal = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, [painting[i][j]])
                normal += 1
    
    visited = [[0] * n for _ in range(n)]
    color_blind = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if painting[i][j] == "R" or painting[i][j] == "G":
                    color = ["R", "G"]
                else:
                    color = ["B"]
                bfs(i, j, visited, color)
                color_blind += 1
                
    print(normal, color_blind)
