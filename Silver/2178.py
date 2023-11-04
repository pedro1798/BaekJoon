import sys
from collections import deque
input = sys.stdin.readline

#칸을 셀 때는 시작 위치와 도착 위치도 포함
row, col = map(int, input().split())
matrix = [list(int(char) for char in input().rstrip()) for _ in range(row)]

def bfs(matrix: list, row: int, col: int):
    visited = [0 for _ in range(row)]
    visited[0] |= (1 << 0)
    predecessor = [list(0 for _ in range(col)) for _ in range(row)]
    
    dx_dy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for x, y in dx_dy:
            if (0 <= i + x < row) and (0 <= j + y < col):
                n_i = i + x
                n_j = j + y
            else:
                continue
            
            if matrix[n_i][n_j] and not (visited[n_i] & (1 << n_j)):                
                visited[n_i] |= (1 << n_j)
                predecessor[n_i][n_j] = predecessor[i][j] + 1
                q.append((n_i, n_j))
                
    return predecessor[-1][-1] + 1

print(bfs(matrix, row, col))
