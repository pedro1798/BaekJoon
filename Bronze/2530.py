from sys import stdin as ss

h, m, s = map(int, ss.readline().split())
add_sec = int(ss.readline())

result = 3600 * h + 60 * m + s + add_sec

new_h = (result // 3600) % 24
new_m = ((result % 3600) // 60) % 60
new_s = (((result % 3600) % 60) // 1) % 60
print(new_h, new_m, new_s)