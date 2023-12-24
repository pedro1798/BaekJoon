import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] == 1 and m[k][j] == 1:
                    m[i][j] = 1
    for i in m:
        print(*i)
