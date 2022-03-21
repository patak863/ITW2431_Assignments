# Name: Mike Patak
# ITW 2431
# Lab 7 Prob. 1
# File name: ITW2431_L7_P1_mpatak.py
# MODIFIED: 3/1/22
# PURPOSE:  The program will take a word as input from the user. The
#       `   program will take the input and convert it to a tuple and it
#           will then count the number of occurrences of each letter in
#           the tuple. The program will output the input as a converted
#           tuple and the number of occurrences of only the letters with
#           more than one occurrence.
# ASSUMPTIONS:  The program will take user input for the word to be used.
###########################################################################

# prompt the user to input a word
str_word = input("The string is: ")
# use the input as input to tuple() to create a new tuple
tuple_letter_cnt = tuple(str_word)
# create dictionary for occurrences
dict_occurrences = {}

# initialize loop counter
int_counter = 0

# while loop to read through the input string
while int_counter < len(tuple_letter_cnt):
    # using string slicing to read each letter in order
    # each time the loop executes
    str_key = tuple_letter_cnt[int_counter]
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
print("The converted tuple is: " + str(tuple_letter_cnt))
for key in dict_occurrences:
    if dict_occurrences[key] > 1:
        print("The repeated letter \"" + str(key) + "\" has "
              + str(dict_occurrences[key]) + " occurrences in tuple")
