import sys
INF = float('inf')
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    area = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]
    
    while True:
        a, b = map(int, input().split())
        if a + b == -2:
            break
        area[a][b], area[b][a] = 1, 1
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if area[i][j] > area[i][k] + area[k][j]:
                    area[i][j] = area[i][k] + area[k][j]
    
    each_area = [area[i] for i in range(1, n+1)]
    max_points = list()
    for area in each_area:
        max_points.append(max(list(filter(lambda x: x!= INF, area))))

    result = list()
    min_point = min(max_points)
    
    for i, e in enumerate(each_area):
        if max(list(filter(lambda x: x!= INF, e))) == min_point:
            result.append(i+1)
            
    print(min_point, len(result))
    print(*sorted(result))
        
