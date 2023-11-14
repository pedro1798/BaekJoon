import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [-1 for _ in range(n + 1)]

def union(a: int, b: int):
    a_root = find(a); b_root = find(b)
    if a_root != b_root:
        if parents[a_root] < parents[b_root]:
            a_root, b_root = b_root, a_root
        parents[a_root] += parents[b_root]
        parents[b_root] = a_root
    
def find(a: int):
    root = a; trail = a
    while parents[root] >= 0:
        root = parents[root]
    while trail != root:
        parents[trail] = root
        trail = parents[trail]
    return root

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    
result = set()
for i in range(1, n + 1):
    result.add(find(i))

print(len(result))
