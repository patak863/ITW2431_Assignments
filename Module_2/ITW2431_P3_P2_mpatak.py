# Name: Mike Patak
# ITW 2431
# Project 3 Prob. 2
# File name: ITW2431_P3_P2_mpatak.py
# MODIFIED: 2/6/22
# PURPOSE:  The program will ask the user to input how many Fibonacci
#           numbers to generate and then generate them. The program will
#           have a function called gen_fib(n) that will generate the
#           Fibonacci numbers and return them as a list. The program
#           Will have a second function called Sum(aList) that take the
#           generated list from genfib(n) and returns the sum of the
#           list. The program will output the Fibonacci sequence and the
#           sum of the all the numbers.
# ASSUMPTIONS:  The Fibonacci sequence will not start with zero.
###########################################################################

# ask the user to input the number of fibonacci numbers to generate
int_num = int(input("How many numbers to generate: "))
# define the variable to hold the result of generated fibonacci list
listResult = list()

# genfib
def genfib(numfib):
    # define the first, second, and sum result variables
    int_first = 0
    int_second = 1
    int_fibSum = 0
    # Initialize loop counter
    int_counter = 0
    int_result = 0
    # initialize the list to hold the fibonacci numbers
    listfibs = list()
    # while loop will execute the number of times depending on the value
    # of the number input by the user
    while int_counter < numfib:
        int_counter += 1
        int_first = int_second
        int_second = int_fibSum
        int_fibSum = int_first + int_second
        # add the fibonacci number to the list
        listfibs.append(int_fibSum)
    # return the result of function
    return listfibs

# function to sum the list of fibonacci numbers
def sum(alist):
    # initialize the counter and int_sum variables
    counter = 0
    int_sum = 0
    # the while loop will iterate through the list of fibonacci numbers
    while counter < len(alist):
        # add the current fibonacci number in the list to the sum
        int_sum += alist[counter]
        # increment counter
        counter += 1
    # return the result of function
    return int_sum


# call the genfib(int_num) function and get a list of fibonacci numbers
listResult = genfib(int_num)
# define the variable for fibonacci string output
str_fibOutput = ''
# define variable for counting the times through loop
int_countLoop = 0
# while loop will load the strings for formatted output
while int_countLoop < len(listResult):
    # cast the element as a 'str' and append a " "
    # then add it to the variable str_fibOutput
    str_fibOutput += str(listResult[int_countLoop]) + " "
    # increment the loop counter
    int_countLoop += 1

# output the results
print("The fibonacci sequence is: " + str_fibOutput)
print("The sum for all numbers is: " + str(sum(listResult)))
