from collections import deque
import sys
input = sys.stdin.readline

def bfs(root: int) -> list:
    visited = 0 | (1 << root)
    depth = [1 if i == root else 0 for i in range(n + 1)]
    q = deque([root])

    while q:
        cur_node = q.popleft()
        for node in graph[cur_node]:
            if not visited & ( 1 << node ):
                visited |= (1 << node)
                depth[node] = depth[cur_node] + 1
                q.append(node)
                
    return depth
    
if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    depth = bfs(1)
    
    for node in range(2, n + 1):
        print(min(graph[node], key = lambda x: depth[x]))
        
