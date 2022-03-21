# Name: Mike Patak
# ITW 2431
# Lab 5 Prob. 1
# File name: ITW2431_P3_P1_mpatak.py
# MODIFIED: 2/17/22
# PURPOSE:  The program will prompt the user to input integer numbers,
#           when the user enters the word 'done' the program will stop
#           taking input. The program will take the integers inputted to
#           create a dictionary. The program will then print out the three
#           largest numbers in the dictionary.
# ASSUMPTIONS:  The data used by the program will be inputted by the user.
###########################################################################

# initialize counter for the numbers of inputs entered
int_key = 1
# create the dictionary
dict_numList = {}

# function to loop through the dictionary to find the maximum 'value'
def max_value():
    # initialize variables int_maxValue and int_maxKey
    int_maxValue = 0
    int_maxKey = 0
    # interate through the dictionary
    for key in dict_numList:
        # check if the current value is greater than int_maxValue
        if int_maxValue < int(dict_numList[key]):
            # assign the value to int_maxValue
            int_maxValue = dict_numList[key]
            # assing the value of the 'key' to int_maxKey
            int_maxKey = key
    # when the for loop completes, use the pop() with int_maxKey
    # to remove the value pair with the max value from the dictionary
    dict_numList.pop(int_maxKey)
    # return the max value
    return int_maxValue

# while loop to prompt the user to enter an integer until the word 'done'
# is entered
while True:
    # prompt the user to input an integer
    int_number = input("Please enter the #" + str(int_key) +
                       " int number until done: ")
    # check if the user enter the word 'done' instead of an integer
    if int_number == 'done':
        # if the user entered 'done' break out of loop
        break
    else:
        # update the dictionary with new key/value pair
        dict_numList.update({int_key: int(int_number)})
    # increment the int_key that counts the number of intergers entered
    int_key += 1

# print out the contents of the dictionary
print(dict_numList)
# create a list to hold the max values
list_maxValues = list()
# initialize loop counter
int_counter = 0
# create the output string to append max values to
str_output = "The 3 largest values are: "
# loop to execute 3 times
while int_counter < 3:
    # calling the max_value() to get max values to
    # concatenate to the str_output
    str_output += str(max_value()) + " "
    # increment the loop counter
    int_counter += 1

# output the 3 largest values in the dictionary
print(str_output)
