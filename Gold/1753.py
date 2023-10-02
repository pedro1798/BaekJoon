import heapq
from sys import stdin as ss

v, e = map(int, ss.readline().split())
#vertex, edge 개수
INF = int(1e9)
start = int(ss.readline()) - 1
#인덱스로 쓰기 위해 -1
graph = [[] for _ in range(v)]
#노드 개수만큼 빈 그래프 생성
    
for i in range(e):
    u, v, w = map(int, ss.readline().split())
    #u에서 v까지 w의 가중치를 가짐
    graph[u-1].append((w, v-1))
    #인덱스 = 노드 번호 - 1
    
def dijkstra(graph, start):
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
    return distances

output = dijkstra(graph,start)
for i in output:
    if i == INF:
        print("INF")
    else:
        print(i)
