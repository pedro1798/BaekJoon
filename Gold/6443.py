import sys
input = sys.stdin.readline

def back_tracking(cnt):
    if cnt == len(words):
        print("".join(ans))
        return
    
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            ans.append(i)
            
            back_tracking(cnt + 1)
            
            visited[i] += 1
            ans.pop()

for i in range(int(input())):
    words = sorted(list(input().rstrip()))
    visited = dict()
    ans = list()
    
    for i in words:
        if i in visited:
            visited[i] += 1    
        else:
            visited[i] = 1
    
    back_tracking(0)
