# Convex Hull

from sys import stdin as ss
import math


class Problem:
    def __init__(self):
        self.n = int(ss.readline())
        self.points = list()
        for _ in range(self.n):
            x, y = map(int, ss.readline().split())
            self.points.append((x, y))
        
    def get_angle(self, pivot: tuple, point: tuple) -> list:
        # return math.atan2(point[1] - pivot[1], point[0] - pivot[0])
        # 기울기가 atan2보다 빠르다
        return math.inf if point[0] == pivot[0] else (point[1] - pivot[1]) / (point[0] - pivot[0])
    
    def ccw(self, a: tuple, b: tuple, c: tuple):
        # 외적의 z성분으로 세 노드의 방향성 도출
        ab = (b[0] - a[0], b[1] - a[1])
        ac = (c[0] - a[0], c[1] - a[1])
        return (ab[0] * ac[1] - ab[1] * ac[0]) > 0
    
    def graham_scan(self, points: list) -> list:
        pivot = min(points, key=lambda x: (x[0], x[1]))
        # 반시계방향 정렬할 기준점
        points.remove(pivot)
        
        sorted_points = sorted(points, key=lambda x: (self.get_angle(pivot, x), x[0], -x[1])) + [pivot]
        # 반시계방향으로 정렬 위해 y값 같으면 x는 오름차순, x값 같으면 y는 내림차순
        # 마지막에 원점과의 비교 위해 [pivot] append

        convex_hull = [pivot, sorted_points.pop(0)]
        
        for item in sorted_points:
            while len(convex_hull) >= 2 and (not self.ccw(convex_hull[-2], convex_hull[-1], item)):
                convex_hull.pop()
            convex_hull.append(item)
            
        convex_hull.pop()
        # 원점과의 비교 끝나면 pop()
        
        return convex_hull
    
    def main(self):
        print(len(self.graham_scan(self.points)))
        
a = Problem()
a.main()
