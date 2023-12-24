import sys
INF = float("inf")
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    kevins = list()
    for i in range(1, n + 1):
        kevin = sum(list(filter(lambda x: x != INF, matrix[i])))
        kevins.append((i, kevin))
    kevins.sort(key = lambda x: (x[1], x[0]))
    
    print(kevins[0][0])
