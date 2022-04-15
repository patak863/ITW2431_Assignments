# Name: Mike Patak
# ITW 2431
# Project 10 Prob. 1
# File name: ITW2431_P10_P1_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "Employee". The class will have the following:
#           method for returning the employees full name, method for applying
#           a raise to their salary, method to display salary before raise,
#           method to display salary after applying raise. The program
#           will output the employees name and salary before and salary after
#           pay raise.
# ASSUMPTIONS:
###############################################################################

# Create class Employee
class Employee:
    # class constructor
    def __init__(self, fname, lname, pay, raise_rate):
        # initialize instance variable
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.raise_rate = raise_rate

    # class method to return the employees full name
    def fullname(self):
        # get the employee full name
        str_fullname = self.fname + " " + self.lname
        # return the employee fullname
        return str_fullname

    # class method to apply pay raise to employee salary
    def apply_raise(self):
        # determine new employee salary
        float_new_pay = round(self.pay * self.raise_rate)
        # return the value of the employees new salary
        return float_new_pay

    # class method to display the employees old and new salary
    def display(self):
        # print out the employees former and new salary
        print("The former salary for " + str(self.fullname()) + " is " + str(self.pay))
        print("The new salary for " + str(self.fullname()) + " is " + str(self.apply_raise()))

# create Employee objects
js = Employee("John", "Smith", 50000, 1.04)
bl = Employee("Bruce", "Lee", 60000, 1.10)
# print the output
js.display()
bl.display()
# Name: Mike Patak
# ITW 2431
# Project 10 Prob. 1
# File name: ITW2431_P10_P1_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "Employee". The class will have the following:
#           method for returning the employees full name, method for applying
#           a raise to their salary, method to display salary before raise,
#           method to display salary after applying raise. The program
#           will output the employees name and salary before and salary after
#           pay raise.
# ASSUMPTIONS:
###############################################################################

# Create class Employee
class Employee:
    # class constructor
    def __init__(self, fname, lname, pay, raise_rate):
        # initialize instance variable
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.raise_rate = raise_rate

    # class method to return the employees full name
    def fullname(self):
        # get the employee full name
        str_fullname = self.fname + " " + self.lname
        # return the employee fullname
        return str_fullname

    # class method to apply pay raise to employee salary
    def apply_raise(self):
        # determine new employee salary
        float_new_pay = round(self.pay * self.raise_rate)
        # return the value of the employees new salary
        return float_new_pay

    # class method to display the employees old and new salary
    def display(self):
        # print out the employees former and new salary
        print("The former salary for " + str(self.fullname()) + " is " + str(self.pay))
        print("The new salary for " + str(self.fullname()) + " is " + str(self.apply_raise()))

# create Employee objects
js = Employee("John", "Smith", 50000, 1.04)
bl = Employee("Bruce", "Lee", 60000, 1.10)
# print the output
js.display()
bl.display()
