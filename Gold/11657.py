import sys
INF = float('inf')
input = sys.stdin.readline

v, e = map(int, input().split());
edges = list(tuple(map(int, input().split())) for _ in range(e))

def bf(start: int):
    dist = [INF if i != start else 0 for i in range(v + 1)]
    for i in range(v):
        for from_node, to_node, weight in edges:
            if dist[from_node] != INF and dist[from_node] + weight < dist[to_node]:
                dist[to_node] = dist[from_node] + weight
                if i == v - 1:
                    return False
    return dist

dist = bf(1)

if dist:
    for i in range(2, v + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)
