import sys
input = sys.stdin.readline

nodes = list()
area = 0

for _ in range(int(input())):
    nodes.append(tuple(map(float, input().split())))
    
x1, y1 = nodes.pop(0)
nodes.append((x1, y1))

for x2, y2 in nodes:
    area += ((x1 + x2) / 2) * (y2 - y1)
    x1 = x2; y1 = y2
    
    
print(area if area >= 0 else -area)
