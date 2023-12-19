import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

# if area[i][j] == 0: 청소 x 빈 칸, elif 1: 벽 
area = list(list(map(int, input().split())) for _ in range(n))


# 0 북쪽 1 동쪽 2 남쪽 3 서쪽

def bfs(x, y, direction):
    cleaned = [0] * (n)
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    block = 0  # 청소하는 칸의 개수
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()  # 현재좌표
        
        if not cleaned[x] & (1 << y):  # 1. 현재 칸이 청소되지 않은 경우
            cleaned[x] |= (1 << y) # 현재 칸을 청소한다.
            block += 1  # 청소한 칸 개수 업데이트
        
        is_all_clean = True
        for dir_x, dir_y in directions:  # 주변 4 칸의 상대위치
            next_x = x + dir_x; 
            next_y = y + dir_y
            if 0 <= next_x < n and 0 <= next_y < m:  # 2. 현재 좌표 주변 4칸 중
                if area[next_x][next_y] != 1 and not (cleaned[next_x] & (1 << next_y)): # for 문을 도는 중 청소되지 않은 빈 칸이 있는 경우
                    direction = (direction - 1) % 4  # 반시계 방향으로 90' 회전
                    forward_x = x + directions[direction][0]
                    forward_y = y + directions[direction][1]
                    if area[forward_x][forward_y] != 1 and (not (cleaned[forward_x] & (1 << forward_y))):  # 바라보는 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우
                        x = forward_x; y = forward_y  # 한 칸 전진한다.
                    q.append((x, y))  # 전진한 결과 업데이트
                    is_all_clean = False
                    break  # for 문을 끝내고 다시 1번으로 돌아간다.
                         
        if is_all_clean:  # 주변에 청소되지 않은 빈 칸이 없는 경우
            backward_x = x + directions[(direction + 2) % 4][0]
            backward_y = y + directions[(direction + 2) % 4][1]  # 후진하는 좌표
            if area[backward_x][backward_y] != 1:  # 방향 유지한 채로 후진할 수 있다면
                q.append((backward_x, backward_y))  # 한 칸 후진하고 1번으로 돌아간다.
            else:  # 후진하지 못한다면:
                return block  # 작동을 멈춘다.
                
print(bfs(x, y, direction))
