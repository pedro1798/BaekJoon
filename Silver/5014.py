import sys
from collections import deque
input = sys.stdin.readline

height, cur_floor, dest_floor, up, down = map(int, input().split())

if cur_floor == dest_floor:
    print(0)
    sys.exit(0)

def bfs(cur_floor: int) -> int:
    floors = set()
    q = deque()
    q.append((cur_floor, 0))
    
    while q:
        cur_floor, button_num = q.popleft()
        for next_floor in (cur_floor - down, cur_floor + up):
            if (1 <= next_floor <= height) and (next_floor not in floors):
                if next_floor == dest_floor:
                    return button_num + 1
                floors.add(next_floor)
                q.append((next_floor, button_num + 1))
                
    return "use the stairs"
                
print(bfs(cur_floor))
