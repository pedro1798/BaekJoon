from sys import stdin as ss
n, m = map(int, ss.readline().split())
m1 = list(list(map(int, ss.readline().split())) for _ in range(n))
m2 = list(list(map(int, ss.readline().split())) for _ in range(n))
m3 = list()
for i in range(n):
    m3.append((list(m1[i][j] + m2[i][j] for j in range(m))))
for i in range(n):
    print(*m3[i])
