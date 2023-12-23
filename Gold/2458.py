import sys
INF = float("inf")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]
    
    for _ in range(m):
        smaller, taller = map(int, input().split())
        matrix[smaller][taller] = 1
    
    for k in range(1, n + 1):  # floyd-warshall O(n^3)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = 1
    count = 0
    for i in range(1, n + 1):
        row_sum = sum(filter(lambda x: x != INF, matrix[i]))
        cols = list(matrix[j][i] for j in range(1, n + 1))
        col_sum = sum(filter(lambda x: x != INF, cols))
        if row_sum + col_sum == n - 1:
            count += 1
            
    print(count)
