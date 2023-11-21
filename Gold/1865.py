import sys
INF = 2000000000
input = sys.stdin.readline
            
            
def bf(edges, start: int) -> bool:
    dist = [0 if i == start else INF for i in range(n + 1)]
    for i in range(n):
        for s, e, t in edges:
            if dist[s] + t < dist[e]:
                if i == n - 1:
                    return "YES"
                dist[e] = dist[s] + t
    return "NO"
    
for _ in range(int(input())):
    n, m, wormholes = map(int, input().split())
    edges = list()
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
        # 도로는 undirected
    for _ in range(wormholes):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
        
    print(bf(edges, 1))
