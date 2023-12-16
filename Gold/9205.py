import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.nodes = list()
        self.n = int(input())
        self.nodes.append(tuple(map(int, input().split()))) # 상근이

        for _ in range(self.n):  # 편의점
            self.nodes.append(tuple(map(int, input().split())))
            
        self.nodes.append(tuple(map(int, input().split()))) # pentaport
   
    def is_reach(self, a, b) -> bool: #manhattan distance
        return (abs(a[0] - b[0]) + abs(a[1] - b[1])) <= 1000
        
    def bfs(self, start, adj_list):
        visited = 0
        q = deque()
        q.append(start)
        
        while q:
            cur = q.popleft()
            
            if cur == self.n + 1:
                print("happy")
                return
                
            if not visited & (1 << cur):
                visited |= (1 << cur)
                
            for next in adj_list[cur]:
                if not visited & (1 << next):
                    visited |= (1 << next)
                    q.append(next)
                    
        print("sad")
        
    def main(self):
        adj_list = [[] for _ in range(self.n + 2)]
        
        for i in range(self.n + 1): # making adj_list
            for j in range(i + 1, self.n + 2):
                if self.is_reach(self.nodes[i], self.nodes[j]):
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        self.bfs(0, adj_list)
         
for _ in range(int(input())):
    Solution().main()
