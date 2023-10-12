# Kruskal

from sys import stdin as ss
import heapq
import math


n, m = map(int, ss.readline().split())
nodes = [0]
q = list()  # min heap
parent = [i for i in range(n + 1)]


def union(a: int, b: int) -> bool:
    root_a = find(a); root_b = find(b)

    if root_a != root_b:  # 같은 그래프에 속하지 않다면
        if root_a > root_b:
            a, b = b, a
        parent[find(b)] = find(a)  # 큰 노드가 작은 노드를 부모로 가진다
        return True  # return True
    return False  # 같은 그래프에 속하면 return False

def find(a: int) -> int:
    if a == parent[a]:
        return a    
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


for _ in range(n):  # i 노드의 x, y 좌표 nodes에 할당
    nodes.append(tuple(map(int, ss.readline().split()))) 


for _ in range(m):  # 이미 연결돼 있는 노드들
    a, b = map(int, ss.readline().split())
    union(a, b)  # union 한다.

for i in range(1, len(nodes)):  # 노드 간 가중치 구하기
    for j in range(i + 1, len(nodes)):
        x1, y1 = nodes[i]; x2, y2 = nodes[j]
        w = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Euclidean distance
        heapq.heappush(q, (w, i, j))  # 가중치 작은 순으로 pop하기 위해 min heap 이용


s = 0  # 가중치 sum
for i in range(len(q)):
    w, n1, n2 = heapq.heappop(q)
    if union(n1, n2):  # 같은 그래프에 속하지 않다면
        s += w
        
# s를 어떻게 소숫점 둘째 자리로 만드느냐    

# 소숫점 셋째 자리까지 formatting
s = "{:.3f}".format(s)

# 셋째 자리에서 반올림 
s = round(float(s), 2)

# 그 결과를 다시 3.00으로 표시
s = "{:.2f}".format(s)

print(s)