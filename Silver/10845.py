import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

def queue(query: str):
    if query[:4] == "push":
        q.append(query[5:])
    elif query == "pop":
        print(q.popleft() if q else -1)
    elif query == "empty":
        print(0 if len(q) else 1)
    elif query == "front":
        print(q[0] if q else -1)
    elif query == "size":
        print(len(q))
    else:
        print(q[-1] if q else -1)
    return
    
for _ in range(n):
    queue(input().rstrip())
