import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited = 0
    q = deque([(start, 0)])
    
    while q:
        cur_node, cur_weight = q.popleft()
        
        if not visited & (1 << cur_node):
            visited |= (1 << cur_node)
        
        for next_node, next_weight in graph[cur_node]:
            if next_node == end:
                return cur_weight + next_weight
            if not visited & (1 << next_node):
                visited |= (1 << next_node)
                q.append((next_node, cur_weight + next_weight))
    return 0
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    query = list()
    
    for _ in range(n-1):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    for _ in range(m):
        query.append(tuple(map(int, input().split())))

    for start, end in query:
        print(bfs(start, end))
