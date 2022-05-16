from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length_variable, breadth_variable):
        self.length = length_variable
        self.breadth = breadth_variable

    def print_area(self):
        return self.length * self.breadth


rec1 = Rectangle(4, 12)
print(f'Area = {rec1.print_area()}.')

# Abstract Method is used to implement a function forcefully.
# Try to comment out the 'print_area' function in the class Rectangle.
# You Cann't make a instance of the abstract calss.Try to dis-comment the following line:-


# rec2 = Shape()