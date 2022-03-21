# Name: Mike Patak
# ITW 2431
# Project 1 Problem 2
# File name: ITW2431_P1_P2_mpatak.py
# MODIFIED: 1/19/22
# PURPOSE:  Program will take as input a number. The number will be
#           how many rows of stars (asterisks) to print out as a pyramid.
# ASSUMPTIONS:  User will only input a number as an integer.
#########################################################################

import textwrap

# Ask the user to input the number of rows to print
int_rows = int(input("Please input the row number: "))

# The function draw_pyramid(num) will take the number enter as input and iterate a while 
# loop that many times. Each time the loop iterates it will build a row of stars. 
def draw_pyramid(num):
    # counter that will keep track of the number of times the loop has been entered
    # and incremented. When the counter equals the input number the loop will exit
    rowCounter = 1
    # The total number of stars and spaces per line
    int_starsNum = num * 2 -1
    # The total number of spaces counter
    int_spaceNum = num -1
    # If the loop1_counter is less than or equal to the number enter the loop again
    while rowCounter <= num:
        # set the loop counter for how many stars to print
        int_spaceCounter = 0
        # initialize the str_row variable before entering the loop
        str_row = ' '
        # initialize the counter for the number of stars per row
        int_starCount = 0
        # 
        while int_starCount < (rowCounter *2 -1):
            str_row = str_row + '*'
            int_starCount = int_starCount + 1
        str_row = textwrap.indent(str_row, ' ' * int_spaceNum)
        print(str_row)

        # decrement the number or spaces counter
        int_spaceNum = int_spaceNum - 1
        # increment the rowCounter
        rowCounter = rowCounter + 1

# Call the draw_pyramid(num) function passing the input number int_rows as a parameter
draw_pyramid(int_rows)
