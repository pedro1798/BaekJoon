from sys import stdin as ss

a = tuple(map(int, ss.readline().split()))
b = tuple(map(int, ss.readline().split()))
c = tuple(map(int, ss.readline().split()))

ca = (c[0] - a[0], c[1] - a[1])
ab = (a[0] - b[0], a[1] - b[1])

def ccw(ca: tuple, ab: tuple) -> bool:
    cross_product = ca[0] * ab[1] - ca[1] * ab[0]
    if cross_product > 0:
        return 1
    elif cross_product == 0:
        return 0
    else:
        return -1

print(ccw(ca, ab))
