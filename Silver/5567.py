import sys
from collections import deque
input = sys.stdin.readline

adj_list = [[] for _ in range(int(input()) + 1)]
visited = [1 if i == 1 else 0 for i in range(len(adj_list))]

for _ in range(int(input())):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        for node in adj_list[cur]:
            if not visited[node]:
                visited[node] = visited[cur] + 1
                q.append(node)

bfs(1)

count_elements = lambda x: sum(1 for i in x if 1 < i <= 3)
print(count_elements(visited))
