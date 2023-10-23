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
    
    def main(self):
        pivot = min(self.points, key=lambda x: (x[0], x[1]))
        self.points.remove(pivot)
        result = ([pivot] + self.angle_sort(pivot, self.points))
        print(len(result))
        for i in result:
            print(*i)
        
a = Problem()
a.main()
