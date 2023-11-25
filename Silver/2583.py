import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
matrix = list([0] * n for _ in range(m))
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x2 -= 1; y2 -= 1  # 끝나는점 인덱스 맞추기
    y1 = (m - 1) - y1  # 매트릭스를 y축으로 위로 뒤집기
    y2 = (m - 1) - y2  # 매트릭스를 y축으로 위로 뒤집기
    
    for i in range(y1, y2 - 1, -1):
        for j in range(x1, x2 + 1):  # 좌하단에서 우상단으로 순회
            if not matrix[i][j]:
                matrix[i][j] = 1
                
def bfs(x, y):
    matrix[x][y] = 1  # 1이 아닐 조건일 때 bfs므로
    q = deque()
    q.append((x, y))
    count = 1  # 빈 공간의 크기
    
    while q:
        x, y = q.popleft()
        for i, j in directions:
            dx = x + i; dy = y + j
            if 0 <= dx < m and 0 <= dy < n:  # boundary condition settings
                if not matrix[dx][dy]:
                    matrix[dx][dy] = 1
                    count += 1
                    q.append((dx, dy))
    return count

result = list()

for i in range(m):
    for j in range(n):
        if not matrix[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)
