# Name: Mike Patak
# ITW 2431
# Lab 2 Prob. 2
# File name: ITW2431_L2_P2_mpatak.py
# MODIFIED: 1/26/22
# PURPOSE:  The program shall have a function 'sum(alist)' that takes
#           a list that contains a set of numbers as a parameter and
#           returns the sum of all the numbers. The output will show
#           the original list and the sum of all the numbers in the list.
# ASSUMPTIONS: The list of numbers to be summed by 'sum(sumlist)' function
#           will be a defined variable in the program.
###########################################################################

# initialize the list variable with a set of numbers
list_num = [1, 21, 3, 12, 9, 10, 14, 30, 24, 6, 8, 18]
# print out the list of numbers
print("list of numbers: " + str(list(list_num)))

# define the function sum(sumList) which will sum all the numbers
# in the list passed as input parameter
def sum(sumList):
    # initialize the loop counter
    count = 0
    # initialize the variable that will hold the sum of all
    # the numbers in the list
    int_sumTotal = 0
    # while loop will iterate through all the numbers in the list
    while count < len(sumList):
        # increment the sum with the value of the current number in the list
        int_sumTotal += sumList[count]
        # increment the loop counter
        count += 1
    # return the sum of all the numbers in the list
    return int_sumTotal

# print the sum of all the numbers in the list
print("The sum of all the numbers in the list is: " + str(sum(list_num)))
