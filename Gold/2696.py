import heapq
from sys import stdin as ss

T = int(ss.readline())
#케이스 수

input = []
#전체 케이스 담은 배열
		
for j in range(T):
	M = int(ss.readline())
	#각 케이으ᅵ 크기
	temp = []
	for k in range(M // 10 + 1):
		temp = temp + (list(map(int, ss.readline().split())))
	#10개씩 끊어서 입력
	input.append(temp)
		

def median(input, n): #배열과 배열 크기 매개벼수
	maxHeap = []
	minHeap = []
	result = []
	
	for i in range(0, n):
		m = input[i]
		if i % 2 == 0: #짝수 번째
			if minHeap and m > minHeap[0]:
				heapq.heappush(maxHeap, -(heapq.heappop(minHeap)))
				heapq.heappush(minHeap, m)
			else:
				heapq.heappush(maxHeap, -m)	
			result.append(-maxHeap[0])
		else: #홀수 번째
			if m < -maxHeap[0]:
				heapq.heappush(minHeap, -(heapq.heappop(maxHeap)))
				heapq.heappush(maxHeap, -m)
			else:
				heapq.heappush(minHeap, m)
				
	return result



for i in range(T):
	output = median(input[i], len(input[i]))
	print(len(output))
	print(*output)