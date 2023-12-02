import math
import sys
input = sys.stdin.readline

monkey, dog = map(int, input().split())

peak = math.floor(math.sqrt(dog - monkey))

if monkey == dog:
    print(0)
elif peak ** 2 == dog - monkey:
    print(peak * 2 - 1)
elif (dog - monkey) - peak ** 2 > peak:
    print(peak * 2 + 1)
else:
    print(peak * 2)
