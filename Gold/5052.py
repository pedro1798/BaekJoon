from sys import stdin as ss

T = int(ss.readline())
for _ in range(T):
    n = int(ss.readline())
    ar = []
    for _ in range(n):
        ar.append(ss.readline().rstrip())
    ar.sort()
    flag = 'YES'
    for i in range(len(ar) - 1):
        if ar[i + 1][:len(ar[i])] == ar[i]:
            flag = 'NO'
    print(flag)
