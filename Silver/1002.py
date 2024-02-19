import sys
input = sys.stdin.readline

def euclidean_dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        x1, y1, smaller_r, x2, y2, bigger_r = map(int, input().split())
        if smaller_r > bigger_r:
            smaller_r, bigger_r = bigger_r, smaller_r

        d = euclidean_dist(x1, y1, x2, y2)

        if x1 == x2 and y1 == y2 and smaller_r == bigger_r:
            print(-1)
        elif bigger_r - smaller_r < d < bigger_r + smaller_r:
            print(2)
        elif bigger_r + smaller_r == d or bigger_r - smaller_r == d:
            print(1)
        else:
            print(0)
