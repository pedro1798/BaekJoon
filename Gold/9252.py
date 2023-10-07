from sys import stdin as ss

s1 = list(ss.readline().strip())
s2 = list(ss.readline().strip())

m = [[0] * (len(s1) + 1) for rows in range(len(s2) + 1)]

def lcs(s1: list, s2: list) -> int:
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:  # 문자가 같다면
                m[i][j] = m[i-1][j-1] + 1
            else:  # 문자가 다르다면
                m[i][j] = max(m[i-1][j], m[i][j-1])
    return m[-1][-1]
    
    
def lcs_find(i: int, j: int) -> int:
    length = m[-1][-1]
    result = list()
    while len(result) < length:
        if m[i-1][j] == m[i][j]:
            i -= 1
        elif m[i][j-1] == m[i][j]:
            j -= 1
        else:
            result.append(s1[j-1])
            i -= 1; j -= 1
    return ''.join(_ for _ in reversed(result))


print(lcs(s1, s2))
print(lcs_find(len(s2), len(s1)))

