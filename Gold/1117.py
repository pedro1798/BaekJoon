import sys
input = sys.stdin.readline

if __name__ == "__main__":
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
    x1 += f; x2 += f
    
    right_dx = 0;
    left_dx = 0;
    dy = (y2 - y1)
    
    if 2 * f >= x2:
        left_dx = (x2 - x1)
    elif 2 * f <= x1:
        left_dx = 0
    else:
        left_dx = 2 * f - x1
        
    if x1 >= W:
        right_dx = 0
    elif x2 <= W:
        right_dx = (x2 - x1)
    else:
        right_dx = (W - x1)
        
    left = (c + 1) * left_dx * dy
    right = (c + 1) * right_dx * dy
    
    print(W * H - (left + right))