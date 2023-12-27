import sys
from collections import deque
input = sys.stdin.readline


def move_cloud(d, s):
    is_rain = list()  # 비가 내리는 위치
    while clouds:
        cx, cy = clouds.popleft()
        cx = (cx + (delta[d][0] * s)) % n;
        cy = (cy + (delta[d][1] * s)) % n
        # 모든 구름이 d 방향으로 s칸 이동한다.
        area[cx][cy] += 1
        # 구름이 있는 칸의 바구니에 저장된 물의 양 1 증가
        is_rain.append((cx, cy))  # 움직인 구름의 위치를 저장
    
    for cx, cy in is_rain:  # 구름이 있는 위치에 물복사마법
        duplicate_magic = 0
        for dx, dy in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
            nx = cx + dx; ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > 0:
                    duplicate_magic += 1
        area[cx][cy] += duplicate_magic
    
    for i in range(n):
        for j in range(n):
            if not (i, j) in is_rain:
                if area[i][j] >= 2:
                    area[i][j] -= 2
                    clouds.append((i, j))
                    
if __name__ == "__main__":
    delta = ((0, 0), (0, -1), (-1, -1), (-1, 0), 
             (-1, 1),(0, 1), (1, 1), (1, 0), (1, -1))
    n, m = map(int, input().split())
    clouds = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
    
    area = [list(map(int, input().split())) for _ in range(n)]
    q = [tuple(map(int, input().split())) for _ in range(m)]
    
    while q:
        d, s = q.pop(0)  # direction, length
        move_cloud(d, s)
        
    result = sum(sum(i) for i in area)
    print(result)
