from sys import stdin as ss
m = [[] for _ in range(15)]

for i in range(5):
    text = ss.readline().rstrip()
    for i, c in enumerate(text):
        m[i].append(c)

for i in m:
    if not i:
        break
    print(''.join(i), end = '')
