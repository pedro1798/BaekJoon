import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    entry_point = None
    stack = deque([(start, start)])
    
    while stack:
        prev, cur = stack.pop()
        
        if not visited[cur]:
            visited[cur] = True
            
        if entry_point is not None:
            break
        
        for next in graph[cur]:
            if next != prev:  # 한 방향으로 진행을 강제하는 조건문
                if not visited[next]:
                    stack.append((cur, next))
                else:  # next가 prev가 아닌데 visited라면 사이클의 진입점이다.
                    entry_point = next
                    break
    
    return entry_point

def bfs(start, end):
    visited = 0
    q = deque([(start, 0)])
    while q:
        cur, depth = q.popleft()
        if not visited & (1 << cur):
            visited |= (1 << cur)
        if cur == end:
            return depth
        for next in graph[cur]:
            if not visited & (1 << next):
                q.append((next, depth + 1))

if __name__ == "__main__":
    v = int(input())
    graph = [[] for _  in range(v + 1)]
    
    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v + 1):
        visited = [True if j == i else False for j in range(v + 1)]
        print(bfs(i, dfs(i)), end = " ")
