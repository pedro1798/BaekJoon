def check(b, c):
    if int(b) > 17 or int(c) >= 80:
        return "Senior"
    return "Junior"
    
while True:
    a, b, c = input().split()
    
    if a == "#":
        break
        
    print(f'{a} {check(b, c)}')
