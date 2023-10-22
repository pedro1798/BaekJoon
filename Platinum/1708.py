# Fucking Convex Hull

from sys import stdin as ss
import math


class Problem:
    def __init__(self):
        self.n = int(ss.readline())
        self.points = list()
        for _ in range(self.n):
            x, y = map(int, ss.readline().split())
            self.points.append((x, y))
        
    def get_inclination(self, pivot: tuple, point: tuple) -> list:
        return math.inf if pivot[0] == point[0] else ((point[1] - pivot[1]) / (point[0] - pivot[0]))
    
    def ccw(self, a: tuple, b: tuple, c: tuple):
        ab = (b[0] - a[0], b[1] - a[1])
        ac = (c[0] - a[0], c[1] - a[1])
        return (ab[0] * ac[1] - ab[1] * ac[0]) > 0
    
    def graham_scan(self, points: list) -> list:
    
        pivot = min(points, key=lambda x: (x[0], x[1]))
        points.remove(pivot)
        
        sorted_points = sorted(points, key=lambda x: (self.get_inclination(pivot, x), x[0], x[1]))

        convex_hull = [pivot, sorted_points.pop(0)]
        
        for item in sorted_points:
            while len(convex_hull) >= 2 and (not self.ccw(convex_hull[-2], convex_hull[-1], item)):
                convex_hull.pop()
            convex_hull.append(item)
            
        return convex_hull
    
    def main(self):
        print(len(self.graham_scan(self.points)))
        
a = Problem()
a.main()
