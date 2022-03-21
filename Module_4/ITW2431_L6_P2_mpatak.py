# Name: Mike Patak
# ITW 2431
# Lab 6 Prob. 2
# File name: ITW2431_L6_P2_mpatak.py
# MODIFIED: 2/24/22
# PURPOSE:  The program will get an integer from the user for the number
#           of exponents of 2 and 3 to calculate. The program will create
#           a tuple of power of 2 exponents and a tuple holding the power
#           of 2 and power of 3 exponents. The program will also calulate
#           and additional power of 2 ** n+1 and add it to the power of
#           2 tuple. The program will output the power of 2 tuple, the
#           power of 2 ** n+1 tuple, and tuple of both power of 2 and
#           power of 3 tuple.
# ASSUMPTIONS:  The user will be prompted to enter an exponent number.
###########################################################################

# prompt the user to enter an exponent number
int_num = int(input("Please enter the exponent number: "))
# initialize loop counter
int_counter = 1
# create two lists, one for exponents of two and one 'list_combined'
# to hold exponents of two and three in order
list_of_twos = list()
list_combined= list()
# initialize the integers for the computed exponents
int_exp2 = 0
int_exp3 = 0
# iterate through the loop for the number of exponents entered
# by user in int_num
while int_counter <= int_num:
    # calculate the power of 2 exponent
    int_exp2 = 2 ** int_counter
    # calculate the power of 3 exponent
    int_exp3 = 3 ** int_counter
    # append the power of 2 exponent to list_of_twos
    list_of_twos.append(int_exp2)
    # append the power of 2 exponent to the list_combined
    list_combined.append(int_exp2)
    # append the power of 3 exponent to the list_combined
    list_combined.append(int_exp3)
    # increment loop counter
    int_counter += 1

# using the list_of_twos create the tuple holding the
# power of 2 exponents
tuple_of_twos = tuple(list_of_twos)
# output the power of 2 exponent tuple
print("(1) The old tuple is: " + str(tuple_of_twos))

# calculate 2 ** n+1 and append to the 'list_of_twos'
list_of_twos.append(2 ** int_counter)
# using the new list_of_twos update the tuple holding the
# power of 2 exponents
tuple_of_twos = tuple(list_of_twos)
# output the new power of 2 exponent tuple
print("(2) The new tuple is: " + str(tuple_of_twos))

# using the list_combined create the tuple that will hold
# the power of 2 and power of 3 exponents in order
tuple_combined = tuple(list_combined)
# output the power of 2 and power of 3 exponent tuple
print("(3) The new tuple is: " + str(tuple_combined))
