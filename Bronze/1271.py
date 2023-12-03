a, b = map(int, input().split())
if a < b:
    a, b = b, a
print(f"{a // b}\n{a % b}")
