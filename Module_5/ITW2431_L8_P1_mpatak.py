# Name: Mike Patak
# ITW 2431
# Lab 8 Prob. 1
# File name: ITW2431_L8_P1_mpatak.py
# MODIFIED: 3/8/22
# PURPOSE:  The program has a function for checking if a string has any
#           non-alphanumeric characters. The program will use regular
#           expression findall() to check the string for non-alphanumeric
#           characters and if it finds any return them as a list. The
#           program will an output for no non-alphanumeric characters
#           found and an output if there are non-alphanumeric characters
#           found.
# ASSUMPTIONS:  The three strings used by the program are hard coded
#               in the program.
###########################################################################

# import the regular expression module
import re

# initialize the test strings
str_1 = "ABCDEFabcdef123450"
str_2 = "ABCDEF;abcdef'1234!50"
str_3 = "*&%@#!}{"

# function to check if a string contains any non-alphanumeric chars
def check_string(str_check):
    print("string: " + str_check)
    # find all occurrences of non-alphanumeric chars in the string as a list
    list_result = re.findall('[^a-zA-Z0-9]', str_check)
    # if the length of the list is equal to zero then no non-alphanumeric
    # chars found
    if len(list_result) == 0:
        # print the no alphanumeric chars found output
        print("The string doesn't contain any non_alphanumeric chars")
    else:
        # print the non-alphanumeric chars found output
        print("The string contains non_alphanumeric chars: " + str(list_result))
    print()

# program purpose
print("The program will check if a string contains any non-alphanumeric characters.\n")
# call the check_string() function for each of the three test strings
check_string(str_1)
check_string(str_2)
check_string(str_3)
