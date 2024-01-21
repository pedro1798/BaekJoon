import sys
input = sys.stdin.readline

def bs(l, r, targ):
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > targ:
            r = mid - 1
        elif nums[mid] < targ:
            l = mid + 1
        else:
            print("1")
            return
    print("0")
    
if __name__ == "__main__":
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    m = int(input())
    targs = tuple(map(int, input().split()))
    
    for targ in targs:
        bs(0, n-1, targ)
