import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
papers = [0, 0]

def divide_and_conquer(matrix: list):
    l = len(matrix)
    flag = is_paper(matrix)
    if flag == "white":
        papers[1] += 1
        return
    elif flag == "black":
        papers[0] += 1
        return
        
    right_up = [matrix[i][l // 2:] for i in range(0, l // 2)]
    left_up = [matrix[i][:l // 2] for i in range(0, l // 2)]
    left_down = [matrix[i][:l // 2] for i in range(l // 2, l)]
    right_down = [matrix[i][l // 2:] for i in range(l // 2, l)]
    divide_and_conquer(left_up)
    divide_and_conquer(right_up)
    divide_and_conquer(left_down)
    divide_and_conquer(right_down)
    
def is_paper(matrix: list):
    result = 0
    l = len(matrix)
    for i in matrix:
        result += sum(i)
    if result == l ** 2:
        return "white"
    elif not result:
        return "black"
        
    return False
    
divide_and_conquer(matrix)
for i in papers:
    print(i)
