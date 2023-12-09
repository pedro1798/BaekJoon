import sys
input = sys.stdin.readline

d, n = map(int, input().split())  # 오븐 깊이, 피자 개수
oven = list(map(int, input().split()))  # 오븐 지름
pizza = list(map(int, input().split()))  # 피자 지름

for i in range(1, d):
    if oven[i - 1] < oven[i]:
        oven[i] = oven[i - 1]

f = 0
for i in range(d - 1, -1, -1):
    if pizza[f] <= oven[i]:
        f += 1
    if f == n:
        print(i + 1)
        break

if f != n:
    print(0)
