from sys import stdin as ss

n, e = map(int, ss.readline().split())
parent = [i for i in range(n+1)]
q = list()


for i in range(e):
    q.append(tuple(map(int, ss.readline().split())))


q.sort(key=lambda x: x[2])


def union(a: int, b: int) -> bool:
    root_a = find(a); root_b = find(b)

    if root_a != root_b:  # 같은 그래프에 속하지 않다면
        if root_a > root_b:
            a, b = b, a
        parent[find(b)] = find(a)
        return True
    return False


def find(a: int) -> int:
    if a == parent[a]:
        return a    
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]
    

def Kruskal(q: list) -> int:
    t = 0
    for a, b, w in q:
        if union(a, b):
            t += w
    return t


print(Kruskal(q))
