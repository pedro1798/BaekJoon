import sys
import math
input = sys.stdin.readline

n = int(input())
nodes = [int(input()) for _ in range(n)]
number_of_each_node = [0] * (max(nodes) + 1)
for i in nodes:
    number_of_each_node[i] += 1
    
toktok = [0] * (n)

for i in range(n):
    a = 1
    while a <= math.sqrt(nodes[i]):
    # n = sqrt(m) * sqrt(m)이다.
    # n = a * b (a, b 는 자연수)가 성립할 조건:
    # 1. a = srqt(n), b = sqrt(n); 2. a < sqrt(n) , b > sqrt(n); 3. a > sqrt(n), b < sqrt(n)
    # n % a (0 < a <= sqrt(n)) == 0 이면 a는 n의 약수. 
        if nodes[i] % a == 0:
            if a != math.sqrt(nodes[i]):
                toktok[i] += number_of_each_node[a] + number_of_each_node[nodes[i] // a]  # nodes[i] // a == b
            else:
                toktok[i] += number_of_each_node[a]
        a += 1
       
for i in toktok:
    print(i - 1)
