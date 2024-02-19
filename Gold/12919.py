import sys
from collections import deque
input = sys.stdin.readline

def add_a(s: str):
    T = list(s)
    T.append('A')
    return "".join(T)
    
def add_b(s: str):
    T = list(s)
    T.append('B')
    return "".join(T[::-1])

def get_pi(p: str):
    n = len(p); j = 0
    pi = list(0 for _ in range(n))
    for i in range(1, n):
        while(j > 0 and p[i] != p[j]):
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi
    
def kmp(p: str, t: str):  # pattern and text
    p_len = len(p); t_len = len(t); j = 0
    pi = get_pi(p)
    
    for i in range(0, t_len):
        while(j > 0 and t[i] != p[j]):
            j = pi[j - 1]
        if t[i] == p[j]:
            if j == p_len - 1:
                return True
            else:
                j += 1
    return False
                    
if __name__ == "__main__":
    s = input().rstrip()
    t = input().rstrip()
    rt = t[::-1]
    
    boundary = len(t)
    answer = 0
    
    q = deque([s])
    
    while q:
        ns = q.popleft()
        
        if not (kmp(ns, t) or kmp(ns, rt)):
            continue
            
        if ns == t:
            answer = 1
            break
            
        if len(ns) > boundary:
            continue
        
        q.append(add_a(ns))
        q.append(add_b(ns))
        
    print(answer)