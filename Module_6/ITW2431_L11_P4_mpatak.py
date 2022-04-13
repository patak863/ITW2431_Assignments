# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 4
# File name: ITW2431_L11_P4_mpatak.py
# MODIFIED: 3/31/22
# PURPOSE:  Create a class named "Rectangle". The class will have two
#           methods, calc_perimeter() and calc_area(). There will be a
#           subclass of Rectangle named Square. The program will use
#           length and width to calculate the area of the rectangle.
#           The program will use the length of the side of a square to
#           calculate the area and perimeter of the square.
# ASSUMPTIONS:
###########################################################################

# define the class Circle
class Rectangle:
    # class constructor
    def __init__(self, width, length):
        # initialize the variable radius
        self.width = width
        self.length = length

    # class method to calculate the perimeter of a cirle
    def calc_perimeter(self):
        # calculate the perimeter using class instance variable
        float_perimeter = round(self.width * 2 + self.length * 2, 2)
        # return the calculated perimeter
        return float_perimeter

    # class method to calculate the area of a circle
    def calc_area(self):
        # calculate the area using class instance variable
        float_area = round(self.width * self.length, 2)
        # return the calculated area
        return float_area


class Square(Rectangle):
    # class constructor
    def __init__(self, length):
        # initialize the variable radius
        self.length = length
        self.width = length


# initialize the rectangle variables

int_rect_length = int(input("Please enter the length of the rectangle: "))
int_rect_width = int(input("Please enter the width of the rectangle: "))
int_sq_length = int(input("Please enter the length of the side of the square: "))
print()
# create the Rectangle object 'r'
r = Rectangle(int_rect_width, int_rect_length)
# print the output, calling the area() method
print("Area of a Rectangle with length " + str(r.length) +
      " and width " + str(r.width) + " is: " + str(r.calc_area()))

# create the Square object
s = Square(int_sq_length)

print("Area of a Square with length " + str(s.length) +
      " is: " + str(s.calc_area()))
# print the perimeter of a Square
print("Perimeter of a Square with length " + str(s.length) +
      " is: " + str(s.calc_perimeter()))

