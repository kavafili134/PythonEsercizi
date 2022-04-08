from cmath import sqrt


class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x,self.y,self.z = x,y,z

# @property
# def x(self):
#     return self.x
# @property
# def y(self):
#     return self.y
# @property
# def z(self):
#     return self.z
# @x.setter
# def x(self,value):
#     self.x = value
# @y.setter
# def y(self,value):
#     self.y = value
# @z.setter
# def z(self,value):
#     self.z = value

def __add__(self,other):
    x = self.x + other.x
    y = self.y + other.y
    z = self.z + other.z
    return Vector(x,y,z)

def __mul__(self,other):
    return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

# def __pitagora(self):
# return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

def __str__(self):
    return"({0},{1},{2})".format(self.x,self.y,self.z)

def __eq__(self,other):
    return Vector(self.x == other.x,self.y == other.y,self.z == other.z)

def __repr__(self):
    rep = 'Vector(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
    return rep

v = Vector(1,2,10)
print(v + Vector(10,12,20))
print(v * Vector(10,12,20))
print(v == Vector(10,12,20))