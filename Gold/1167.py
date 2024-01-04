import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(root, visited, dist):
    if not visited & (1 << root):
            visited |= (1 << root)
    for node, weight in adj_list[root]:
        if not visited & (1 << node):
            visited |= (1 << node)
            dist[node] = dist[root] + weight
            dfs(node, visited, dist)

def solution():
    # x에서 가장 먼 노드 y는 트리의 지름을 이루는 두 노드 u, v 중 하나에 무조건 속한다.
    # y와 y에서 가장 먼 노드는 트리의 지름을 이룬다.
    dist_from_x = [0] * (n + 1)
    dfs(1, 0, dist_from_x)
    y = dist_from_x.index(max(dist_from_x))
    dist_from_y = [0] * (n + 1)
    dfs(y, 0, dist_from_y)
    diameter_of_tree = max(dist_from_y)
    print(diameter_of_tree)
    
if __name__ == "__main__":
    n = int(input())  # 노드의 개수
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(n):
        query = list(map(int, input().split()))
        parent = query[0];
        for i in range(1, len(query) - 1, 2):
            child = query[i]; weight = query[i + 1]
            adj_list[parent].append((child, weight))
            adj_list[child].append((parent, weight))
            
    solution()
