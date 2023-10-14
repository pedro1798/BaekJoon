from sys import stdin as ss

a, b, c = map(int, ss.readline().split())

def fast_exponentiation(base: int, expon: int, modulus: int) -> int:
    result = 1
    base %= modulus
    while expon > 0:
        if expon & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        expon >>= 1
    return result

answer = fast_exponentiation(a, b, c)
print(answer)

