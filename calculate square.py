import math
class square():
    def __init__(self, side_length):
        self.side_length = side_length
    def print_side_length(self):
        print(self.side_length)
    def area(self):
        return self.side_length ** 2
    def __add__(self, side_increase): 
        square2 = square(self.side_length + side_increase)
        return(square2)
s = square(3) 
print(f"Side Length: {s.side_length}")
print(f"Area: {s.area()}")
new_square = s + 2
print(f"New Side Length: {new_square.side_length}")
print(f"New Area: {new_square.area()}")