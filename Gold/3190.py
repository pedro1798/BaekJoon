import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

apples = list()

for _ in range(k):
    a, b = map(int, input().split())
    apples.append((a-1, b-1))

to_x, to_y = (0, 1)

dirs = deque()  # 뱀 방향 쿼리
for _ in range(int(input())):
    a, b = input().split()
    dirs.append((int(a), b))

snake = [(0, 0)]
sec = 0

q = deque()
q.append((0, 0))

cnt, query = dirs.popleft()

while q:  # bfs
    x, y = q.pop()  # snake의 머리

    if sec == cnt:  # 움직일 시간이면 방향을 바꾼다
        if query == "L":
            if to_x == 0 and to_y == 1:
                to_x, to_y = -1, 0
            elif to_x == -1 and to_y == 0:
                to_x, to_y = 0, -1
            elif to_x == 0 and to_y == -1:
                to_x, to_y = 1, 0
            else:
                to_x, to_y = 0, 1

        else:
            if to_x == 0 and to_y == 1:
                to_x, to_y = 1, 0
            elif to_x == 1 and to_y == 0:
                to_x, to_y = 0, -1
            elif to_x == 0 and to_y == -1:
                to_x, to_y = -1, 0
            else:
                to_x, to_y = 0, 1

        if dirs:
            cnt, query = dirs.popleft()  # 다음 쿼리 popleft

    x, y = x + to_x, y + to_y  # snake의 머리에서 다음 블럭으로 이동

    if ((x, y) in snake) or (0 > x or x >= n) or (0 > y or y >= n):  # 이동할 위치가 충돌한다면
        sec += 1
        break  # while문을 탈출한다

    q.append((x, y))  # 충돌하지 않는다면 머리를 움직인다
    snake.append((x, y))

    if (x, y) not in apples:  # 사과를 안 먹었다면
        snake.pop(0)  # 그렇지 않다면 한 칸 이동한다.
    else:
        apples.remove((x, y))

    sec += 1

print(sec)
