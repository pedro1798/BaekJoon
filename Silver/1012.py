from collections import deque
import sys
input = sys.stdin.readline

class Problem:
    def __init__(self):
        self.n, self.m, k = map(int, input().split())
        self.field = list([0] * self.n for _ in range(self.m))
        for _ in range(k):
            x, y = map(int, input().split())
            self.field[y][x] = 1
        self.visited = list(0 for _ in range(self.m))
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
    def bfs(self, i: int, j: int):
        q = deque()
        q.append((i, j))
        self.visited[i] |= (1 << j)
        
        while q:
            i, j = q.popleft()
            for x, y in self.directions:
                nx = i + x; ny = j + y
                if 0 <= nx < self.m and 0 <= ny < self.n:
                    if not self.visited[nx] & (1 << ny) and self.field[nx][ny]:
                        self.visited[nx] |= (1 << ny)
                        q.append((nx, ny))
        return
            
    def main(self):
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i] & (1 << j) and self.field[i][j]:
                    self.bfs(i, j)
                    count += 1
        print(count)
        
for _ in range(int(input())):
    Problem().main()
        
