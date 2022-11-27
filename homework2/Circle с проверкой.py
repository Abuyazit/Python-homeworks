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
n = 2

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
Xv, Yv =2, 2
assert(circle(2).radius())==2
assert(circle(2).diameter())==4
assert(circle(2).__len__())==12.566370614359172
assert(circle(2).area())==12.566370614359172
assert(circle(2).newrad())==4
assert((circle(2)*circle(n)).rad)==315.82734083485946

assert(circle1(2, 2).center())==(2,2)
assert(circle1(2, 2).moving())==(4,4)
assert(circle1(2, 2).distance())== 5.656854249492381
