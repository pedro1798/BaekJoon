import sys
from collections import deque
input = sys.stdin.readline


def bfs(root, rm):
    q = deque([root])
    count = 0
    visited = 0
    
    while q:
        cur = q.popleft()
        if not visited & (1 << cur):
            visited |= (1 << cur)
        if cur == rm:
            continue
            
        if not tree[cur] or tree[cur] == [rm]:
            count += 1
            
        for child in tree[cur]:
            if not visited & (1 << child):
                q.append(child)
                visited |= (1 << child)
    
    print(count)


if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n)]
    for i, e in enumerate(list(map(int, input().split()))):
        if e == -1:
            root = i
        else:  # i의 부모 e
            tree[e].append(i)
    rm = int(input())
    bfs(root, rm)
