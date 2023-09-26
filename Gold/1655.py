import heapq
from sys import stdin as ss

n = int(ss.readline())
input = []

for _ in range(n):
	input.append(int(ss.readline()))
		

maxHeap = []
minHeap = []

for i in range(0, n):
	n = input[i]
	if i % 2 == 0:		
		if minHeap and n > minHeap[0]:
			heapq.heappush(maxHeap, -(heapq.heappop(minHeap)))
			heapq.heappush(minHeap, n)
		else:
			heapq.heappush(maxHeap, -n)	
	else:
		if n < -maxHeap[0]:
			heapq.heappush(minHeap, -(heapq.heappop(maxHeap)))
			heapq.heappush(maxHeap, -n)
		else:
			heapq.heappush(minHeap, n)
	print(-maxHeap[0])