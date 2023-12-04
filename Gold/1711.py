import sys, math
input = sys.stdin.readline

n = int(input())
points = list(tuple(map(int, input().split())) for _ in range(n))
rectangles = 0

def power_of_euclidean_distance(a: tuple, b: tuple):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

for a in range(0, n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            ab = power_of_euclidean_distance(points[a], points[b])
            bc = power_of_euclidean_distance(points[b], points[c])
            ca = power_of_euclidean_distance(points[c], points[a])
            if max(ab, bc, ca) * 2 == ab + bc + ca:
                rectangles += 1
            
print(rectangles)
