import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cows = [[] for _ in range(n + 1)]
    count = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if not cows[a]:
            cows[a].append(b)
        else:
            if cows[a][0] ^ b:
                cows[a][0] = b
                count += 1
        
    print(count)
