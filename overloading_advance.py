import math

class Circle():
    def __init__(self,radius):
        self.__radius = radius
    def getradius(self):
        self.__radius = radius
    def setradius(self):
        self.__radius = radius
    def area(self):
        return math.pi * self.__radius ** 2
    def __add__(self,next_circle):
        return Circle( self.__radius + next_circle.__radius)
    def __gt__(self,next_circle):
        return self.__radius > next_circle.__radius
    def __lt__(self,next_circle):
        return self.__radius < next_circle.__radius
    def __str__(self):
        return "hello , get lost"

c1 = Circle(10)
c2 = Circle(20)

print c3 > c2

