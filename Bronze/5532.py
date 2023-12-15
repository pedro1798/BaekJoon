import sys
import math
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input()) 
c = int(input())
d = int(input())

print(l - max(math.ceil(a / c), math.ceil(b / d)))