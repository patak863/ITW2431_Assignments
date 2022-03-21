# Name: Mike Patak
# ITW 2431
# Lab 3 Prob. 2
# File name: ITW2431_L3_P2_mpatak.py
# MODIFIED: 2/3/22
# PURPOSE:  The program will prompt the user to input a list of numbers
#           and stores them in a list using a loop. The program and will
#           then print the maximum and minimum numbers after the loop
#           completes.
# ASSUMPTIONS:  Numbers will be inputed by the user until the word 'done'
#               is entered.
##########################################################################

# initialize the list that will hold the input numbers
list_numbers = list()

# The while loop will read the input from command line until the word 'done' is
# entered. The while loop will take the numbers from input and append to a list.
# During the loop the maximum and minimum numbers will be determined.
while True:
    # Ask the user to input the course name
    str_input = input("Enter a number: ")
    if str_input == 'done':
        break
    else:
        list_numbers.append(float(str_input))

print(list_numbers)
print("Maximum: " + str(max(list_numbers)))
print("Minimum: " + str(min(list_numbers)))
