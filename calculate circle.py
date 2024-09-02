import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    def print_radius(self):
        print(self.radius)
    def circumference(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
    def __add__(self, radius_increase):
        circle2 = circle(self.radius +radius_increase)
        return(circle2)
c = circle(2)  
print(f"Radius: {c.radius}")
print(f"Area: {c.area()}")
new_circle = c+3  
print(f"New Radius: {new_circle.radius}")
print(f"New Area: {new_circle.area()}")