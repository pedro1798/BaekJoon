from sys import stdin as ss
import math


def dfs(root: int, visited: list, adj_list: list, dp: list) -> int:
    if not visited[root]:  # visited False면
        visited[root] = True
        for child in adj_list[root]:  # root의 자식 노드들
            if not visited[child]:
                dp[child][0] = root
                depth[child] = depth[root] + 1
                dfs(child, visited, adj_list, dp)

                
def lca(n: int, m: int, dp: list, depth: list) -> int:  # longest common ancestor
    if depth[n] > depth[m]:  # n이 높은 수, m이 깊은 수
        n, m = m, n
    diff = depth[m] - depth[n]
    k = 0
    while diff:
        if diff & 1:
            m = dp[m][k]
        diff >>= 1
        k += 1
    if n == m:
        return n
    while dp[n][0] != dp[m][0]:  # 부모 노드가 다르면
        n = dp[n][0]; m = dp[m][0] 
    
    return dp[n][0]

N = int(ss.readline())  # 노드 1~N
adj_list = [list() for i in range(N + 1)]  # 인접 리스트
depth = [0 for i in range(N + 1)]  # 깊이 array

    
for i in range(N - 1):  # 인접 리스트로 트리 초기화
    n, m = map(int, ss.readline().split())
    adj_list[min(n, m)].append(max(n, m))

visited = [False for _ in range(N + 1)]
dp = [[0] * 17 for nodes in range(N + 1)]
dfs(1, visited,adj_list, dp)

    
M = int(ss.readline())  # LCA 찾을 노드쌍 개수

nodes = []  # LCA 찾을 노드쌍 입력
for i in range(M):
    nodes.append(tuple(map(int, ss.readline().split())))

# dp table 채움
# math.ceil(log2(트리의 높이)) 만큼만 dp테이블 채우면 됨.
max_height = math.ceil(math.log2(max(depth)))
for k in range(max_height):
    for node in range(1, N + 1):
        dp[node][k + 1] = dp[dp[node][k]][k]
        

for n, m in nodes:
    print(lca(n, m, dp, depth))
