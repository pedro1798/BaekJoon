# Knuth-Morris-Pratt O(N + M)

from sys import stdin as ss

text = list(ss.readline().rstrip('\n'))
pattern = list(ss.readline().rstrip('\n'))

def getPi(pattern: list) -> list:
    pi = [0] * len(pattern)
    length = 0; i = 1
    while i < len(pattern):
        if pattern[length] == pattern[i]:
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
    i = 0  # text index
    j = 0  # pattern index
    result = list()
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                result.append(i - j + 1)
                j = pi[j-1]  # for next matches
        else:
            if j:
                j = pi[j-1]
            else:
                i += 1
    return result

result = kmp(text, pattern)
print(len(result))
print(*result)
