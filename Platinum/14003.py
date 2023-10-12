from sys import stdin as ss
n = int(ss.readline())
a = list(map(int, ss.readline().split()))

def binary_search(result: list, target: int) -> int:
    l = 0; r = len(result) - 1
    while l <= r:
        m = (l + r) // 2
        if result[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l
    

def lis(a: list):
    result = [a[0]]
    index = [0] * len(a)
    for i in range(1, len(a)):
        if a[i] > result[-1]:
            index[i] = len(result)
            result.append(a[i])
        else:
            insert = binary_search(result, a[i])
            index[i] = insert
            result[insert] = a[i]
            
    s = list()
    count = len(result) - 1
    for j in range(len(a) - 1, -1, -1):
        if index[j] == count:
            s.append(a[j])
            count -= 1
    print(len(result))
    print(*reversed(s))
    
lis(a)
