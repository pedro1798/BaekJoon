import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cows = list(input().rstrip())
    state = [0 for _ in range(26)]
    save_state = [0 for _ in range(26)]
    q = deque()
    count = 0
    
    for cow in cows:
        i = abc.index(cow)
        if not state[i]:  # toggle 이전 0: 소는 목초지로 들어가기 전이다.
            pre = int(''.join(map(str, state)), 2)
            save_state[i] = pre  # 들어가기 이전의 목초지 상태 저장
        
        state[i] ^= 1  # 소의 state toggle
        
        if not state[i]:  # toggle 이후 0: 목초지에서 빠져나왔다.
            pre = save_state[i]  # last in first out
            post = int(''.join(map(str, state)), 2)
            count += sum(list(map(int, bin(pre & ~post)[2:])))
            
    print(count)
