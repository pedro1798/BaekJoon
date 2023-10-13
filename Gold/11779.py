# Dijkstra

import heapq
from sys import stdin as ss
INF = int(1e9)

vertex, edge = map(int, ss.readline().split())
# vertex, edge 개수

graph = [[] for _ in range(vertex)]
# 노드 개수만큼 빈 그래프 생성

for i in range(edge):
    u, v, w = map(int, ss.readline().split())
    # u에서 v까지 w의 가중치를 가짐
    graph[u-1].append((w, v-1)); graph[v-1].append((w, u-1))
    # undirected weighted graph

transit1, transit2 = map(int, ss.readline().split())
# 경유할 노드
transit1 -= 1; transit2 -= 1
    
def dijkstra(start: int, end: int) -> int:
    distances = [INF for _ in graph]
    distances[start] = 0
    q = [(0, start)]

    while q:
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node] < current_distance:
            continue
        for weight, neighbor in graph[current_node]:
            distance_to_neighbor = current_distance + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(q, (distance_to_neighbor, neighbor))
    return distances[end]

case1 = dijkstra(0, transit1) + dijkstra(transit1, transit2) + dijkstra(transit2, vertex - 1)
# 1 -> transit1 -> transit2 -> n
case2 = dijkstra(0, transit2) + dijkstra(transit2, transit1) + dijkstra(transit1, vertex - 1)
# 1 -> transit2 -> transit1 -> n
result = min(case1, case2)
print("-1" if result >= INF else result)
