import sys
input = sys.stdin.readline

times = list()
for _ in range(int(input())):
    times.append(tuple(map(int, input().split())))

times.sort(key = lambda x: (x[1], x[0]))
result = [times.pop(0)]

for time in times:
    if time[0] >= result[-1][1]:
        result.append(time)

print(len(result))
