import sys
sys.setrecursionlimit(1000000)
from sys import stdin as ss
LOG = 17

n = int(ss.readline())  # 노드 수

g = [[] for _ in range(n + 1)]  # 인접 리스트
for _ in range(n - 1):  # 인접 리스트 초기화
    a, b = map(int, ss.readline().split())
    g[a].append(b);  g[b].append(a)
    

d = [0 for _ in range(n + 1)]  # 각 노드 깊이
c = [False for _ in range(n + 1)]  # visited check

dp = [[0] * LOG for u in range(n + 1)]  # dp[u][k]


def dfs(root: int):
    c[root] = True
    for child in g[root]:
        if not c[child]:  # child 방문 안했으면
            d[child] = d[root] + 1  # child depth 초기화
            dp[child][0] = root  # dp 부모 초기화
            dfs(child)

dfs(1)
def make_dp():
    for k in range(LOG - 1):
        for u in range(1, n + 1):
            dp[u][k + 1] = dp[dp[u][k]][k]
            
make_dp()

    
def lca(a: int, b: int):
    if d[a] > d[b]:  # a가 더 깊다면
        a, b = b, a
    dif = d[b] - d[a]
    k = 0
    while dif:
        if dif & 1:
            b = dp[b][k]
        dif >>= 1
        k += 1
    if a == b:
        return a
    
    for i in range(LOG - 1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]; b = dp[b][i]
    return dp[a][0]


m = int(ss.readline())
for _ in range(m):
    a, b = map(int, ss.readline().split())
    print(lca(a, b))
