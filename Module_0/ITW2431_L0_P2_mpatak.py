# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 2
# File name: ITW2431_L0_P2_mpatak.py
# MODIFIED: 1/12/22
# PURPOSE:  Try various values to see which will output the values:
#           ab, a, b, c, Python is fun!
# ASSUMPTIONS:

# import sys, so that input arguments can be accessed using the arg variable
import sys

# parse the input
# the variable 'a' will store the numeric input from command line
a = int(sys.argv[1])
# print out the value of 'a'
print("a = " + str(a))
# based on the value of 'a' the if/elif/else decision tree will print a, b, or c
if a > 10 and a % 6 = 3:
    print("a")
elif a > 10 and a < 20:
    print("b")
else:
    print("c")
