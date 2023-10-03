from sys import stdin as ss

n = int(ss.readline())
e = int(ss.readline())
INF = float('inf')

graph = [[0 if i == j else INF for j in range(n)] for i in range(n)]
#자기 자신으로의 가중치는 0, 나머진 INF로 그래프 초기화

for i in range(e):
    u, v, w = map(int, ss.readline().split())
    if graph[u-1][v-1] > w:
        graph[u-1][v-1] = w
    #한 노드에서 다른 노드로의 간선이 여러 개일 수 있으므로 가중치가 최소인 경우로 입력값 할당
    #인덱스로 사용 위해 -1


def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    #k를 경유해서 가는 거리가 짧다면 짧은 거리 그래프에 할당
    return graph


output = floyd_warshall(graph)

for i in range(n):
    graph[i] = [0 if x == INF else x for x in graph[i]]
    #이어지지 않은 graph[i]][j] == INF 값을 0으로 출력
    print(*graph[i])
