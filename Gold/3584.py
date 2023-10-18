# LCA O(logN)

import sys
sys.setrecursionlimit(1000000)
ss = sys.stdin
LOG = 17
t = int(ss.readline())


class Problem:
    def __init__(self):
        self.n = int(ss.readline())  # 노드 수
        self.graph = [[] for _ in range(self.n + 1)]  # 인접 리스트 for dfs
        self.dp = [[0] * LOG for u in range(self.n + 1)]  # 2^0, 2^1, 2^2..번째 부모 노드 담을 dp
        for i in range(1, self.n):  # adjacency graph initiation, 간선 수는 n - 1
            a, b = map(int, ss.readline().split())  # a is parent, b is child
            self.dp[b][0] = a  # b의 2^0번째 부모는 a
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.first, self.second = map(int, ss.readline().split())  # LCA 찾을 두 노드

        self.depth = [0 for _ in range(self.n + 1)]
        # list for saving depth of each nodes
        for i in range(1, self.n + 1):  # 부모가 0인 루트 노드 찾기
            if self.dp[i][0] == 0:
                self.root = i

    def dfs(self, root: int, visited: int):  # dfs로 depth assign
        visited |= (1 << root)  # visited[root] = True
        for child in self.graph[root]:
            if not (visited & (1 << child)):  # if child is not visited
                self.depth[child] = self.depth[root] + 1
                self.dfs(child, visited)

    def make_dp(self):  # dp 배열 채우는 함수
        for k in range(LOG - 1):
            for u in range(1, self.n + 1):
                self.dp[u][k + 1] = self.dp[self.dp[u][k]][k]

    def lca(self, a: int, b: int) -> int:  # Lowest Common Ancestor
        if self.depth[a] > self.depth[b]:  # a가 높은(depth 작은) 노드이다
            a, b = b, a
        dif = self.depth[b] - self.depth[a]
        k = 0
        while dif:
            if dif & 1:
                b = self.dp[b][k]
            dif >>= 1
            k += 1
        if a == b:
            return a

        for k in range(LOG - 1, -1, -1):
            if self.dp[a][k] != self.dp[b][k]:
                a = self.dp[a][k]
                b = self.dp[b][k]
        return self.dp[a][0]

    def main(self):
        self.dfs(self.root, 0)
        self.make_dp()
        print(self.lca(self.first, self.second))


for _ in range(t):
    test_case = Problem()
    test_case.main()