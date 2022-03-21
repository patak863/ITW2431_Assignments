# Name: Mike Patak
# ITW 2431
# Lab 2 Prob. 3
# File name: ITW2431_L2_P3_mpatak.py
# MODIFIED: 1/26/22
# PURPOSE:  The program has a function 'max(alist)' that takes a list
#           that contains a set of numbers as a parameter and returns
#           the max of all the numbers. The output will show the
#           original list and the output of the 'max(alist)' the max
#           number from the list.
# ASSUMPTIONS: The list of numbers that the 'max(alist)' function will
#           examine will be a defined variable in the program.
# ##########################################################################

# initialize the list variable with a set of numbers
list_num = [1, 21, 3, 12, 9, 10, 14, 30, 24, 6, 8, 18]
# print out the list of numbers
print("list of numbers + " + str(list(list_num)))


# function max(maxList) will find the number with the highest value
def max(maxList):
    # initialize the loop counter
    int_count = 0
    int_maxVal = 0
    # the while loop will process through the list of numbers to find the
    # number with the highest value
    while int_count < len(maxList):
        # if this is first time through the loop assign
        # int_maxVal the first element in the list
        if int_count == 0:
            int_maxVal = maxList[int_count]
        # if int_maxVal is less than the current element in the list
        # assign int_maxVal the current element in the list
        elif int_maxVal < maxList[int_count]:
            int_maxVal = maxList[int_count]
        # increment the loop counter
        int_count += 1
    # return the value of int_maxVal
    return int_maxVal

# print out the number in the list with the maximum value
print("The number with the max value is: " + str(max(list_num)))
