# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 1
# File name: ITW2431_L10_P1_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "Circle". The class will have two
#           methods, calc_perimeter() and calc_area(). The program will
#           use two values for the radius and calculate the perimeter and
#           area based on the radius. The program will output the radius
#           value, the calculated perimeter, and the calculated area.
# ASSUMPTIONS:
###########################################################################

# define the class Circle
class Circle:
    # class constructor
    def __init__(self, num):
        # initialize the variable radius
        self.radius = num

    # class method to calculate the perimeter of a cirle
    def calc_perimeter(self):
        # calculate the perimeter using class instance variable
        float_perimeter = round(2 * 3.14 * self.radius, 2)
        # format the float to always show to significant digits
        format_perimeter = "{:.2f}".format(float_perimeter)
        # return the calculated perimeter
        return format_perimeter

    # class method to calculate the area of a circle
    def calc_area(self):
        # calculate the area using class instance variable
        float_area = round(3.14 * self.radius * self.radius, 2)
        # format the float to always show to significant digits
        format_area = "{:.2f}".format(float_area)
        # return the calculated area
        return format_area

# initialize the first radius
int_radius = 1
# create the Circle object 'c'
c = Circle(int_radius)
# print the output, calling the area() and perimeter() methods
print("Your circle with radius " + str(c.radius) +
      " inch has an area " + str(c.calc_area()) +
      " and a perimeter of " + str(c.calc_perimeter()) + ".")
# assign the class variable the second radius value of 5
c.radius = 5
# print the output, calling the area() and perimeter() methods
print("Your circle with radius " + str(c.radius) +
      " inch has an area " + str(c.calc_area()) +
      " and a perimeter of " + str(c.calc_perimeter()) + ".")

