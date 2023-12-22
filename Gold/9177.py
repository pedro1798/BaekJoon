import sys
from collections import deque
input = sys.stdin.readline

def is_interleaving():
    rows = len(s1); cols = len(s2)
    
    visited = [[0] * (cols) for _ in range(rows)]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for flag, d in enumerate(delta):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny]:
                    if flag == 0 and (s1[nx] == s3[nx + ny]):  
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                    if flag == 1 and (s2[ny] == s3[nx + ny]):
                        visited[nx][ny] = 1
                        q.append((nx, ny))
    
    return visited[-1][-1]

if __name__ == "__main__":
    delta = ((1, 0), (0, 1))
    for i in range(1, int(input()) + 1):
        s1, s2, s3 = map(lambda x: [False] + list(x), input().rstrip().split())  # False is margin
        print(f"Data set {i}: {'yes' if is_interleaving() else 'no'}")
        
