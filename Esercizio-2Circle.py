import math
from turtle import circle
class Circle:
    def __init__(self,_radius):
        self.radius = _radius
    
    def get_area(self):
        return (math.pi * (self.radius ** 2))
    
    def __repr__(self):
        rep = 'Circle(' + str(self.radius) + ', area:' + str(self.get_area()) + ')'
        return rep
    
    def __add__(self,other):
        return Circle(self.radius + other.radius)
    
    def __lt__(self,other):
        return self.radius < other.radius

    def __gt__(self,other):
        return self.radius > other.radius
    
    def __eq__(self,other):
        return self.radius == other.radius
    
    def getRadius(self):
        return self.radius
    



circle1 = Circle(6)
circle2 = Circle(9)
print(repr(circle1))
print(repr(circle1+circle2))
print(circle1 < circle2)
print(circle1 > circle2)
print(circle1 == circle2)

c = Circle(7)
circles =[circle1, circle2, c, circle1 + c, circle1 + circle2]

print(circles)
circles.sort()
print(circles)