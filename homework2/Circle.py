import math
class circle:
    def __init__(self, rad):
        self.rad = rad
    def radius(self):
        return self.rad
    def diameter(self):
        return self.rad*2
    def __len__(self):
        return 2 * math.pi * self.rad
    def area(self):
        return math.pi * self.rad**2
    def newrad(self):
        return self.rad * n
    def __mul__(self, other):
        return circle((2 * math.pi * self.rad)*(2 * math.pi *(other.rad * self.rad)))
rad = int(input())
n = int(input())
z = circle(rad)*circle(n)
obj = circle(rad)
print(obj.radius(),
      obj.diameter(),
      obj.__len__(),
      obj.area(),
      obj.newrad(),
      z.rad, sep='\n')


class circle1(circle):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def center(self):
        return self.x, self.y
    def moving(self):
        x=self.x + Xv
        y=self.y + Yv
        return x, y
    def distance(self):
        return ((self.x + Xv)**2 + (self.y + Yv)**2) ** 0.5
c1, c2 = map(int, input().split())
Xv, Yv = map(int, input().split())
obj_2=circle1(c1, c2)
print(obj_2.center(),
      obj_2.moving(),
      obj_2.distance(), sep='\n')











    


