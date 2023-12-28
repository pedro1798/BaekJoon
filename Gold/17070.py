import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline

def is_line(x1, y1, x2, y2):
    if y1 == y2:
        return 0  # vertical
    elif x1 == x2:
        return 1  # horizontal
    return 2  # diagonal

def is_ok(x1, y1, x2, y2):
    if is_line(x1, y1, x2, y2) != 2:
        if grid[x2][y2] == 1:
            return False
    else:
        for dx, dy in ((-1, 0), (0, 0), (0, -1)):
            nx, ny = x2 + dx, y2 + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    return False
            else:
                return False
    return True

def dfs(x1, y1, x2, y2):
    global count
    if x2 == n - 1 and y2 == n - 1:
        count += 1
        return
    line = is_line(x1, y1, x2, y2)
    
    for dx, dy in delta[line]:
        nx, ny = x2 + dx, y2 + dy
        if 0 <= nx < n and 0 <= ny < n and is_ok(x2, y2, nx, ny):
            dfs(x2, y2, nx, ny)
    
if __name__ == "__main__":
    count = 0
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    delta = (
        ((1, 0), (1, 1)),
        ((0, 1), (1, 1)),
        ((0, 1), (1, 0), (1, 1))
    )
    
    if grid[n-1][n-1] == 1:
        print(0)
    else:
        dfs(0, 0, 0, 1)
        print(count)
