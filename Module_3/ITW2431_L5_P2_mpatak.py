# Name: Mike Patak
# ITW 2431
# Lab 5 Prob. 2
# File name: ITW2431_P3_P1_mpatak.py
# MODIFIED: 2/17/22
# PURPOSE:  The program will take a word as input from the user and it
#           will then count the number of occurrences of each letter. The
#           program will output the letter followed by the number of
#           occurrences.
# ASSUMPTIONS:  The program will take user input for the word to be used.
###########################################################################

# prompt the user to input a word
str_word = input("Please type a string to count for letter occurrence: ")

# create dictionary for occurrences
dict_occurrences = {}

# initialize loop counter
int_counter = 0

# while loop to read through the input string
while int_counter < len(str_word):
    # using string slicing to read each letter in order
    # each time the loop executes
    str_key = str_word[int_counter:int_counter + 1]
    # check to see if the current letter is already a dictionary key
    if str_key in dict_occurrences:
        # if the key already exists, increment the value of
        # the key/value pair
        dict_occurrences[str_key] = dict_occurrences[str_key] + 1
    # if the key does not already exist in the dictionary
    else:
        # if the current letter does not already exist as a dictionary key
        # create 'dict_temp' as a temporary dictionary for the purpose of updating
        # the 'dict_occurrences' using the str_key and set the initial value to 1
        dict_temp = {str_key: 1}
        # update 'dict_occurrences'
        dict_occurrences.update(dict_temp)
    # increment the loop counter
    int_counter += 1

# print the output
print(dict_occurrences)
