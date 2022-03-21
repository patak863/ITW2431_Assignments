# Name: Mike Patak
# ITW 2431
# Lab 8 Prob. 2
# File name: ITW2431_L8_P2_mpatak.py
# MODIFIED: 3/8/22
# PURPOSE:  The program has a function for checking if a string fits a
#           specific pattern. The pattern being searched for is the
#           starts with a upper case letter, followed by all lower case
#           letters. The program will then output whether or not a string
#           matched the pattern or not.
# ASSUMPTIONS:  The strings used are hard coded in the program.
###########################################################################

# import the regular expression module
import re

# initialize the test strings
str_1 = "aaB_cbbbc"
str_2 = "aaBAbbbc"
str_3 = "Aaab_abbbc"
str_4 = "Aaababbbc"

# function for checking if the string contains a specific pattern
def check_string(str_check):
    print("string: " + str_check)
    # the regular expression search() function is used to check
    # if the input string matches the pattern.
    if re.search(r'^[A-Z][a-z]+$', str_check):
        # If a match is found print out "Found a match!"
        print("Found a match!")
    else:
        # if a match is not found print out "Not Matched!"
        print("Not matched!")
    print()

# program purpose
print("The program will check if a string starts with one upper case character followed by all lower case characters.\n")
# call the check_string() function for each of the test strings
check_string(str_1)
check_string(str_2)
check_string(str_3)
check_string(str_4)
