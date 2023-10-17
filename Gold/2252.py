from sys import stdin as ss
from collections import deque

n, e = map(int, ss.readline().split())
digraph = [list() for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(e):
    from_node, to_node = map(int, ss.readline().split())
    digraph[from_node].append(to_node)
    indegree[to_node] += 1

    
def topologycal_sort(digraph: list, indegree: list) -> list:
    result = list()
    q = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    while q:
        current_node = q.popleft()
        result.append(current_node)
        for node in digraph[current_node]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
    if len(result) == len(digraph) - 1:
        return result
    else:
        raise ValueError("There're cycle in the digraph.")
        
try:
    print(*topologycal_sort(digraph, indegree))
except ValueError as e:
    print(e)

