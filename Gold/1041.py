import sys


def solve(a, b, c, d, e, f):
    one = min(a, b, c, d, e, f)
    x, y, z = min(a, f), min(e, b), min(c, d)
    two = x + y + z - max(x, y, z)
    three = min(a, f) + min(d, c) + min(e, b)
    if n == 1:
        print(sum((a, b, c, d, e, f)) - max(a, b, c, d, e, f))
    else:
        print( one * (5 * (n ** 2) - 16 * n + 12) + two * (8 * n - 12) + three * 4 )
    
    
if __name__ == "__main__":
    n = int(input())
    solve(*map(int, input().split()))
