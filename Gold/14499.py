import sys
input = sys.stdin.readline

map_row, map_col, x, y, q = map(int, input().split())

matrix = list(list(map(int, input().split())) for _ in range(map_row))
    
queries = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
# index 1이 위, 3이 아래
def paint(x, y):
    if matrix[x][y] != 0:
        dice[3] = matrix[x][y]
        matrix[x][y] = 0
    else:
        matrix[x][y] = dice[3]
    print(dice[1])
            
for query in queries:
    temp = dice[:]
    if query == 1:  # 동쪽
        if 0 <= y + 1 < map_col:
            y += 1  # 주사위 좌표를 옮기고
            dice[5], dice[4], dice[1], dice[3] = temp[1], temp[3], temp[4], temp[5]
            
            paint(x, y)
    elif query == 2:  # 서쪽
        if 0 <= y - 1 < map_col:
            y -= 1
            dice[4], dice[5], dice[3], dice[1] = temp[1], temp[3], temp[4], temp[5]
            
            paint(x, y)
    elif query == 3:  # 북쪽
        if 0 <= x - 1 < map_row:
            x -= 1
            dice[3], dice[0], dice[1], dice[2] = temp[0], temp[1], temp[2], temp[3]
            
            paint(x, y)
    else:  # 남쪽
        if 0 <= x + 1 < map_row:
            x += 1
            dice[1], dice[2], dice[3], dice[0] = temp[0], temp[1], temp[2], temp[3]
            
            paint(x, y)
        
