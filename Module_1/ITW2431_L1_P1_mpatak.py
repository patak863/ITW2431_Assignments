# Name: Mike Patak
# ITW 2431
# Lab 1 Prob. 1
# File name: ITW2431_L1_P1_mpatak.py
# MODIFIED: 1/19/22
# PURPOSE:  Program will take as input a number. The number will be
#           how many rows of stars (asterisks) to print out as a triangle.
# ASSUMPTIONS:  User will only input a number as an integer.
#############################################################################

# Ask the user to input the number of rows to print
int_rows = int(input("Please input the row number: "))

# The function draw_star(num) will take the number enter as input and iterate a while
# that many times. Each time the loop iterates it will build a string of stars. For example
# the first time through it will print "*", the second time through it will print "**"
# so that the number of stars in the last line printed will equal the input number.
def draw_star(num):
    # counter that will keep track of the number of times the loop has been entered
    # and incremented. When the counter equals the input number the loop will exit
    loop1_counter = 1
    # If the loop1_counter is less than or equal to the number enter the loop again
    while loop1_counter <= num:
        # set the loop counter for how many stars to print
        loop2_counter = 0
        # initialize the str_star variable before entering the loop
        str_star = ''
        # Check if the counter for the while loop is less than the loop1_counter
        # and if it is, enter the loop again
        while loop2_counter < loop1_counter:
            # concatenate str_star with a "*" each time the loop executes
            str_star = str_star + '*'
            # increment the loop2_counter to track number of times loop has run
            loop2_counter = loop2_counter + 1
        # after the second while loop is done print out str_star
        print(str_star)
        # increment the loop1_counter
        loop1_counter = loop1_counter + 1

# Call the draw_star(num) function passing the input number int_rows as a parameter
draw_star(int_rows)
