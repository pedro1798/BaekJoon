from collections import deque
from sys import stdin as ss

def dfs(root):
    visited[root] = True
    print(root, end=" ")
    for i in graph[root]:
        if not visited[i]:
            dfs(i)

def bfs(root):
    visited = [False] * (n + 1)
    queue = deque([root])
    visited[root] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m, root = map(int, ss.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y); graph[y].append(x)

for i in graph:
    i.sort()

visited = [False] * (n + 1)
dfs(root)
print()
bfs(root)
