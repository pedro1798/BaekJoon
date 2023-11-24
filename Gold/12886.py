import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b, c):
    sum_of_rocks = a + b + c
    visited=[[False] * sum_of_rocks for _ in range(sum_of_rocks)]

    if sum_of_rocks % 3:  # 필요조건: 돌 개수의 합이 3의 배수이다.
        return 0
    
    q = deque()
    q.append((a, b))
    visited[a][b] = True  # 돌 개수의 합은 불변이기에 두 수만 비교해도 상관없다.
    
    while q:
        a, b = q.popleft(); c = sum_of_rocks - a - b
        if a == b == c:  # 돌 개수의 합이 3의 배수일 때 a == b == c 라면:
            return 1
            
        for x, y in (a, b), (a, c), (b, c):
            if x == y:  # 돌 개수 같다면 비교할 수 없음
                continue
            if x > y:  # x < y
                x, y = y, x
            y -= x; x *= 2; z = sum_of_rocks - x - y
            
            if not visited[x][y]:
                q.append((x, y))
                visited[x][y] = True
    return 0

print(bfs(*tuple(map(int, input().split()))))
