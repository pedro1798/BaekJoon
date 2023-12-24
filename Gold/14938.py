import sys
INF = float('inf')
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, r = map(int, input().split())
    items = tuple(map(int, input().split()))
    area = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]

    for _ in range(r):
        a, b, w = map(int, input().split())
        area[a][b], area[b][a] = w, w
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if area[i][j] > area[i][k] + area[k][j]:
                    area[i][j] = area[i][k] + area[k][j]
    
    max_item = 0
    for i in range(1, n+1):
        sum = 0  
        for j in range(1, n + 1):
            if area[i][j] <= m:
                sum += items[j - 1]
        max_item = max(max_item, sum)
    print(max_item)