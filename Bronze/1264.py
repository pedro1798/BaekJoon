import sys
input = sys.stdin.readline

vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
while True:
    string = input().rstrip()
    if string == "#":
        break
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    print(count)
