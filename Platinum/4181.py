from sys import stdin as ss
import math

class Problem:
    def __init__(self):    
        self.n = int(ss.readline())
        self.points = list()
        for _ in range(self.n):
            x, y, flag = ss.readline().split()
            if flag == 'Y':
                self.points.append((int(x), int(y)))
    
    def get_angle(self, pivot: tuple, point: tuple) -> float:
        return math.inf if point[0] == pivot[0] else (point[1] - pivot[1]) / (point[0] - pivot[0])
    
    def angle_sort(self, pivot: tuple, points: list) -> list:
        return sorted(points, key=lambda x:(self.get_angle(pivot, x), -x[1], x[0]))
    
    def ccw(self, a: tuple, b: tuple, c: tuple):
        ab = (b[0] - a[0], b[1] - a[1])
        ac = (c[0] - a[0], c[1] - a[1])
        return ab[0] * ac[1] - ab[1] * ac[0] > 0
    
    def graham_scan(self, points: list):
        pivot = min(points, key=lambda x: (x[0], x[1]))
        points.remove(pivot)
        
        sorted_points = self.angle_sort(pivot, points)
        convex_hull = [pivot, sorted_points.pop(0)]
        
        for item in sorted_points:
            while len(convex_hull) >= 2 and (not self.ccw(convex_hull[-2], convex_hull[-1], item)):
                convex_hull.pop()
            convex_hull.append(item)
            
        return convex_hull
    
    def main(self):
        pivot = min(self.points, key=lambda x: (x[0], x[1]))
        self.points.remove(pivot)
        result = ([pivot] + self.angle_sort(pivot, self.points))
        print(len(result))
        for i in result:
            print(*i)
        
a = Problem()
a.main()
