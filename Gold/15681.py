import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def count_subtree_nodes(root):
    visited[root] = True
    for node in tree[root]:
        if not visited[node]:
            sizes[root] += count_subtree_nodes(node)
    
    return sizes[root]

if __name__ == "__main__":
    n, r, q = map(int, input().split())
    tree = [[] for _ in range(n + 1)]
    queries = list()
    sizes = [1 for _ in range(n + 1)]
    visited = list(False for _ in range(n + 1))

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for _ in range(q):
        queries.append(int(input()))
    
    count_subtree_nodes(r)

    for query in queries:
        print(sizes[query])
    