import sys
input = sys.stdin.readline

n = int(input())  # 컴퓨터 수
m = int(input())  # 직접 연결된 컴퓨터 쌍 수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y); graph[y].append(x)

visited = [0 for _ in range(n + 1)]

def dfs(root: int) -> list:
    for i in graph[root]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)
    return visited

dfs(1)
sum = -1
for i in visited:
    if i == 1:
        sum += 1
        
print(sum if sum != -1 else 0)
