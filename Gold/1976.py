import sys
input = sys.stdin.readline
            
def is_union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return True
    if a > b:
        a, b = b, a
    parents[b] = a
    return False
    
def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    parents = [i for i in range(n + 1)]
    
    for i in range(n):
        line = list(map(int, input().split()))
        for j, e in enumerate(line):
            if e == 1:
                is_union(i+1, j+1)
                
    path = list(map(int, input().split()))
              
    pivot = path.pop()
    result = "YES"
    for next in path:
        if is_union(pivot, next):
            continue
        result = "NO"
        
    print(result)