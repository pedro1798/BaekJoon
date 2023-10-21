from sys import stdin as ss

n, m = map(int, ss.readline().split())

unheard = set()
unseen = set()
for _ in range(n):
    unheard.add(ss.readline().rstrip())
for _ in range(m):
    unseen.add(ss.readline().rstrip())
    
result = list(unheard & unseen)
print(len(result))
print(*sorted(result))
