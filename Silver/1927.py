from sys import stdin as ss
import heapq

q = list()
for _ in range(int(ss.readline())):
    x = int(ss.readline())
    heapq.heappush(q, x) if x != 0 else print(heapq.heappop(q) if q else 0)
