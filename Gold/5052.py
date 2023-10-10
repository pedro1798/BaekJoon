from sys import stdin as ss

T = int(ss.readline())

for _ in range(T):
    n = int(ss.readline())
    arr = []
    for _ in range(n):
        arr.append(ss.readline().rstrip())
    arr.sort()
    flag = 'YES'
    for i in range(len(arr) - 1):
        if arr[i + 1][:len(arr[i])] == arr[i]:
            flag = 'NO'
    print(flag)
