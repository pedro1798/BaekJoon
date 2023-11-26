import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
iceberg = list(list(map(int, input().split())) for _ in range(n))
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(visited: list, i: int, j: int):
    q = deque()
    q.append((i, j))
    counts = list()  # 주변 바다의 개수
    while q:
        i, j = q.popleft()
        visited[i] |= (1 << j)
        count = 0
        for x, y in directions:
            nx = i + x; ny = j + y
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx] & (1 << ny) and iceberg[nx][ny] > 0:
                    visited[nx] |= (1 << ny)
                    q.append((nx, ny))
                elif iceberg[nx][ny] == 0:
                    count += 1
        counts.append((i, j, count))  # counts에 주변 바다의 개수를 저장한다.
    for i, j, count in counts:  # 일괄적으로 주변 바다의 개수를 각 빙산의 높이에서 뺀다.
        iceberg[i][j] = iceberg[i][j] - count if iceberg[i][j] - count >= 0 else 0
    
    return 1
    
def num_of_chunks_in_next_year():  # bfs를 사용해 iceberg를 1년 후로 업데이트 한다.
    visited = [0 for _ in range(n)]
    num_of_chunks = 0
    for i in range(n):
        for j in range(m):
            if not visited[i] & (1 << j) and iceberg[i][j] > 0:
                num_of_chunks += bfs(visited, i, j)
    return num_of_chunks

def is_zero():  # 빙산이 다 녹았는지 확인한다.
    is_zero = 0
    for i in iceberg:
        is_zero += sum(i)
    return is_zero
    
def count_years():
    years = 0
    while "next_year":
        chunks = num_of_chunks_in_next_year()  # 1년 후 iceberg의 chunk 개수를 리턴한다. iceberg는 이 라인에서 업데이트된다.
        if chunks > 1:  # 빙하가 갈라졌다면
            return years
        else:  # 빙하가 갈라지지 않았다면
            if is_zero():  # 빙하가 갈라지지 않고 다 녹지도 않았다면
                years += 1
            else:  # 빙하가 갈라지지 않은 채 다 녹았다면
                return 0
            

print(count_years())
