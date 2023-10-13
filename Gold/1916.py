# dijkstra

from sys import stdin as ss
import heapq
INF = int(1e9)


n = int(ss.readline())  # 1 ~ N nodes
m = int(ss.readline())  # edges

digraph = [[] for _ in range(n + 1)]  # directed adjacency list

for _ in range(m):
    n1, n2, weight = map(int, ss.readline().split())  # fron n1 to n2 with weight
    digraph[n1].append((weight, n2))  # digraph assign

start, destination = map(int, ss.readline().split())

def dijkstra(digraph: list, start: int, destination: int) -> int:
    distances = [INF for _ in digraph]  # distances graph
    distances[start] = 0  # set start as 0
    q = [(0, start)]  # min heap

    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue
        for weight, neighbor in digraph[current_node]:
            distance_to_neighbor = current_distance + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(q, (distance_to_neighbor, neighbor))
    return distances[destination]

print(dijkstra(digraph, start, destination))
    
    
