# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 3
# File name: ITW2431_L11_P3_mpatak.py
# MODIFIED: 3/31/22
# PURPOSE:  Create a class named "StringStuff". The class will have three
#           methods, get_string(), lower_string(), and upper_string().
#           The program will program will prompt a user for input using
#           the get_string() method. The program will then output the
#           original string. The program will call the lower_string()
#           method and output the string in all lowercase. The program
#           will then call the upper_string() method and output the string
#           in all uppercase.
# ASSUMPTIONS:
###########################################################################

# define the class StringStuff
class StringStuff:
    # class constructor
    def __init__(self):
        # initialize the variable
        self.str_input = ''

    # class method to get string input from the user
    def get_string(self):
        # prompt the user to input a string
        self.str_input = input("Type in a string: ")
        # print out the original string
        print("The original string is: \n" + self.str_input + "\n")

    # class metho to convert the string to all lower case letters
    def lower_string(self):
        print("The converted to lower case for the input is: \n" +
              self.str_input.lower() + "\n")

    # class method to convert the string to all upper case letters
    def upper_string(self):
        print("The converted to upper case for the input is: \n" +
              self.str_input.upper() + "\n")

# create the StringStuff object
s = StringStuff()
# call the StringStuff method get_string()
s.get_string()
# call the StringStuff method get_lower()
s.lower_string()
# call the StringStuff method get_upper()
s.upper_string()
