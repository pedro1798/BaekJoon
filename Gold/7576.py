import sys
from collections import deque
input = sys.stdin.readline
dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
def is_full(n, m, crate):
    for row in crate:
        if 0 in row:
            return False
    return True

def bfs(n, m, crate):  
    q = deque()
    
    for i, row in enumerate(crate):
        for j, item in enumerate(row):  
            if item == 1:
                q.append((i, j))  
                
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx; ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if crate[nx][ny] == 0:
                    crate[nx][ny] = crate[x][y] + 1
                    q.append((nx, ny))
                                  
def solution(n, m, crate):
    bfs(n, m, crate)     
    print(max([max(row) for row in crate]) - 1 if is_full(n, m, crate) else -1) 
    return
    
if __name__ == "__main__":
    m, n = map(int, input().split())
    crate = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, crate)