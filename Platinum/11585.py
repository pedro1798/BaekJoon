from sys import stdin as ss
from fractions import Fraction

n = int(ss.readline())
pattern = list(ss.readline().split())
text = list(ss.readline().split()) * 2
text.pop(-1)

def getPi(pattern: list) -> list:
    pi = [0] * len(pattern)
    i = 1
    length = 0
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            pi[i] = length
            i += 1
        else:
            if length:
                length = pi[length - 1]
            else:
                pi[i] = 0
                i += 1
    return pi


def kmp(text: list, pattern: list) -> list:
    pi = getPi(pattern)
    result = list()
    i = 0  # 텍스트 인덱스
    j = 0  # 패턴 인덱스
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result.append(i - j + 1)
                j = pi[j - 1]
        else:
            if j:
                j = pi[j - 1]
            else:
                i += 1
    return result


numerator = len(kmp(text, pattern))
if numerator == n:
    print("1/1")
else:
    print(Fraction(numerator, n))