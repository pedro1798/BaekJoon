# LIS

from sys import stdin as ss

n = int(ss.readline())
sequence = list(map(int, ss.readline().split()))

def binary_search(result: list, target: int):
    l = 0; r = len(result) - 1
    while l <= r:
        mid = (l + r) // 2
        if result[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

def lis(sequence: list) -> int:  # Longest Increasing Subsequence
    s_length = len(sequence)
    result = [sequence[0]]
    index = list(0 for _ in range(s_length))
    for i in range(1, s_length):
        if sequence[i] > result[-1]:
            index[i] = len(result)
            result.append(sequence[i])
        else:
            insert = binary_search(result, sequence[i])  
            # sequence[i]보다 같거나 큰 값중 가장 작은 값 = sequence[i]
            index[i] = insert  # insert는 삽입할 위치
            result[insert] = sequence[i]
    return index


lis_index = lis(sequence)
reversed_sequence = sequence[::-1]
# sequence를 reverse해서 lis 하면 원래 sequencce의
# Longest Decreasing Subsequence를 구할 수 있다.
lds_index = lis(reversed_sequence)[::-1]

answer = list()
for i in range(n):
    answer.append(lis_index[i] + lds_index[i] + 1)
    

print(max(answer))
