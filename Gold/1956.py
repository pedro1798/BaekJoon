import sys
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
digraph = [list(0 if i == j else INF for i in range(v)) for j in range(v)]

for _ in range(e):
    n, m, w = map(int, input().split())
    digraph[n-1][m-1] = w
    
for k in range(v):
    for i in range(v):
        for j in range(v):
            if digraph[i][j] > digraph[i][k] + digraph[k][j]:
                digraph[i][j] = digraph[i][k] + digraph[k][j]

result = list()
for i in range(v):
    for j in range(v):
        temp = digraph[i][j] + digraph[j][i]
        if 0 < temp < INF:
            result.append(temp)
            
print(min(result) if result else '-1')
