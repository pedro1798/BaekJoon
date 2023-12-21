import sys
from collections import deque
input = sys.stdin.readline

delta = ((), 
         (1, -1), 
         (1, 0), 
         (1, 1), 
         (0, -1), 
         (0, 0), 
         (0, 1), 
         (-1, -1), 
         (-1, 0), 
         (-1, 1))

ard_x, ard_y = 0, 0

crazy_arduino = dict()
board = list()

r, c = map(int, input().split())

for i in range(r):
    line = list(input().rstrip())
    for j, char in enumerate(line):
        if char == "I":
            ard_x, ard_y = i, j
        elif char == "R":
            crazy_arduino[(i, j)] = ["R"]
    board.append(line)

direction = list(map(int, list(input().rstrip())))

def min_manhattan_distance(x1, y1, x2, y2):
    # from (x1, y1) to (x2, y2)
    m = abs(x1 - x2) + abs(y1 - y2)
    min_index = 5  # 움직이지 않을 경우

    for i in range(1, len(delta)):
        next_x, next_y = x1 + delta[i][0], y1 + delta[i][1]
        manhattan_distance = abs(next_x - x2) + abs(next_y - y2)
        if manhattan_distance < m:
            m = manhattan_distance
            min_index = i
            
    return delta[min_index]

def one_move(direction):
    global ard_x; global ard_y;
    
    board[ard_x][ard_y] = "."
    ard_x += delta[direction][0]; 
    ard_y += delta[direction][1]  # JongSu's Arduino
    
    if board[ard_x][ard_y] == "R":  # 만약 아두이노가 미친 아두이노 만나면 
        return False  # 게임 종료
        
    board[ard_x][ard_y] = "I"  # 1. 그렇지 않다면 종수가 아두이노를 이동시킴
    
    temp = [key for key in crazy_arduino.keys()]

    for crz_x, crz_y in temp:  # 움직일 각각의 미친 아두이노
        next_x, next_y = min_manhattan_distance(crz_x, crz_y, ard_x, ard_y)  # 종수의 아두이노와 가장 가까운 방향을 리턴
        next_x += crz_x;  # 종수의 아두이노와 가장 가까운 방향의 좌표
        next_y += crz_y
    
        if board[next_x][next_y] == "I":  # 종수의 아두이노를 만나면
            return False  # 게임 종료
        else:
            board[next_x][next_y] = "R"
            crazy_arduino[(crz_x, crz_y)].pop()
            if (next_x, next_y) in crazy_arduino:
                crazy_arduino[(next_x, next_y)].append("R")
            else:
                crazy_arduino[(next_x, next_y)] = ["R"]
            
    temp = {key: value for key, value in crazy_arduino.items()}
    for key, arduino in temp.items():
        x, y = key
        if not len(arduino) == 1:
            board[x][y] = "."
            crazy_arduino.pop(key, None)
            
    return True

game_over = False

for i, d in enumerate(direction):
    if one_move(d):
        continue
    else:
        print(f"kraj {i + 1}")
        game_over = True
        break
    
if not game_over:
    for line in board:
        print("".join(line))
