# Dijkstra

from sys import stdin as ss
import heapq
INF = int(1e20)

n, m, x = map(int, ss.readline().split())
x -= 1

digraph = [[] for _ in range(n)]  # 0 ~ n-1
reversed_digraph = [[] for _ in range(n)]

for i in range(m):
    from_n, to_n, weight = map(int, ss.readline().split())
    from_n -= 1; to_n -= 1
    digraph[from_n].append((weight, to_n))
    reversed_digraph[to_n].append((weight, from_n))
    
def dijkstra(digraph: list, start: int) -> int:
    q = [(0, start)]
    distances = [0 if i == start else INF for i in range(len(digraph))]
    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue
        for weight, neighbor in digraph[current_node]:
            distance_to_neighbor = weight + current_distance
            if distances[neighbor] > distance_to_neighbor:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(q, (distances[neighbor], neighbor))
                
    return distances


x_to_nodes = dijkstra(digraph, x)
nodes_to_x = dijkstra(reversed_digraph, x)

answer = list()
for i in range(n):
    answer.append(x_to_nodes[i] + nodes_to_x[i])

print(max(answer))