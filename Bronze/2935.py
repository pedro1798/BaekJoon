from sys import stdin as ss
a = list(ss.readline().rstrip() for _ in range(3))
print('1' + '0' * (len(a[0]) + len(a[2]) - 2) if a[1] == "*"  else int(a[0]) + int(a[2]))
