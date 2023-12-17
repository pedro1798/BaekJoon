import sys
input = sys.stdin.readline

p, m = map(int, input().split())

level, nickname = input().split()
rooms = [ [(int(level), nickname)] ]

for _ in range(p - 1):
    level, nickname = input().split()
    level = int(level)
    
    is_entered = False
    
    for room in rooms:
        if len(room) < m and (room[0][0] - 10 <= level <= room[0][0] + 10):  # 자리가 있고 레벨이 맞을 때
            room.append((level, nickname))  # 들어간다
            is_entered = True        
            break
            
    if not is_entered:  # 레벨 맞는 방이 없다면 새로 방을 판다.
        rooms.append([(level, nickname)])
        

for room in rooms:
    room.sort(key = lambda x: (x[1], x[0]))
    
    if len(room) == m:
        print("Started!")
        for i in room:
            print(*i)  # 출력한다.
    else:
        print("Waiting!")
        for i in room:
            print(*i)  # 출력한다.
