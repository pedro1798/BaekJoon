from sys import stdin as ss
n, b = map(int, ss.readline().split());
input = [list(map(int, ss.readline().split())) for _ in range(n)]

def matrixMul(first, second):
    #first, second를 입력받아 행렬곱한 배열 리턴, 매 번 초기화
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] += first[k][j] * second[i][k]
                if (matrix[i][j] >= 1000):
                    matrix[i][j] %= 1000
    return matrix

def fast_power(base, exponent):
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    #unit matrix로 result 초기화
    while exponent:
        if exponent & 1: #exponent가 홀수이면:
            result = matrixMul(result, base)
        base = matrixMul(base, base)
        exponent //= 2
    return result

for i in range(n):
    print(*fast_power(input, b)[i])