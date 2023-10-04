from sys import stdin as ss


n, m = map(int, ss.readline().split())
parent = [-1] * (n + 1)


def collapsing_find(i):  # i의 root 찾기.
    root = i
    while parent[root] >= 0:
        root = parent[root]  # 부모가 음수일 때 까지 루트 타고 올라감
    trail = i
    while trail != root:  # 자취는 root 전까지
        parent[trail] = root  # trail이 지나오는 모든 element 부모 root를 가리키게 collaps
        trail = parent[trail]
    return root    

def weighted_union(i, j):
    i_root = collapsing_find(i); j_root = collapsing_find(j)
    if i_root != j_root:
        if parent[i_root] < parent[j_root]:  # i를 포함한 그래프의 노드 수가 더 많으면
            i_root, j_root = j_root, i_root  # 루트를 서로 바꿔 코드를 축약
        parent[j_root] += parent[i_root]
        parent[i_root] = j_root   
        
        
answer = []
for i in range(m):
    flag, a, b = map(int, ss.readline().split())
    if flag == 1:  # flag == 1
        if collapsing_find(a) == -1 and collapsing_find(b) == -1:
            answer.append("NO")
        elif collapsing_find(a) != collapsing_find(b):
            answer.append("NO")
        else:
            answer.append("YES")
    else:
        weighted_union(a, b)

for i in answer:
    print(i)


