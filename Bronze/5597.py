a = [int(input()) for _ in range(28)]
b = []

for i in range(1, 31):
    if i not in a:
        b.append(i)

print(f"{b[0]}\n{b[1]}" if b[0] < b[1] else f"{b[1]}\n{b[0]}")

