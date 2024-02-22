import sys
input = sys.stdin.readline

def dfs(prev, current):
    global cycle
    if not visited[current]:
        visited[current] = True
    for next in graph[current]:
        if next != prev:  # 한 방향으로만 탐색.
            if not visited[next]:
                visited[next] = True
                dfs(current, next)
            else:  # 부모 노드가 아닌데 방문한 노드라면 사이클이 존재한다.
                cycle = True
    
if __name__ == "__main__":
    TC = 0
    while True:
        TC += 1
        v, e = map(int, input().split())
        cycle = False
        count = 0  # 트리의 개수
        
        if not (v or e):  # 0, 0이면 종료
            break

        visited = [False for _ in range(v + 1)]
        graph = [[] for _ in range(v + 1)]

        for _ in range(e):  # 무향그래프 초기화
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, v + 1):  # 노드 1부터 탐색
            if not visited[i]:  # 지난 번 탐색에서 방문한 노드는 건너뛰기
                dfs(i, i)  # i번 노드부터 dfs
                if not cycle:
                    # 사이클이 없다면 count에 1을 더한다. 사이클이 있다면 무시한다.
                    count += 1
                cycle = False  # for문 안에서 반복하므로 cycle 초기화

        print(f"Case {TC}:", f"No trees." if count == 0 else (f"There is one tree." if count == 1 else f"A forest of {count} trees."))                  
