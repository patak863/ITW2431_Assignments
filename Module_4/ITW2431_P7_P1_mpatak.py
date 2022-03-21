# Name: Mike Patak
# ITW 2431
# Project 7 Prob. 1
# File name: ITW2431_P7_P1_mpatak.py
# MODIFIED: 3/4/22
# PURPOSE:  The program will take a string of input from the user split the
#           string in words that will be loaded into a list. The list will be
#           used to create a tuple of the words. The program will then iterate
#           through the tuple counting the number of occurrences of each word
#           and loading the word and occurrences into a dictionary as a key
#           value pair. The program will out the words that occur more than once.
# ASSUMPTIONS:
##################################################################################

# prompt user for an input string
str_input = input("Please enter a string: ")
# split the input string
list_inputstring = list(str_input.split())
# create a tuple using the split input string
tuple_inputstring = tuple(list_inputstring)
# create dictionary for occurrences
dict_occurrences = {}

# for loop to read through the input string
for str_key in tuple_inputstring:
    # check to see if the current word is already in the dictionary
    if str_key in dict_occurrences:
        # if the key already exists, increment the value of
        # the key/value pair
        dict_occurrences[str_key] += 1
    # if the key does not already exist in the dictionary
    else:
        # the current word does not already exist, add as a dictionary key
        dict_occurrences[str_key] = 1

# print the output
for key in dict_occurrences:
    if dict_occurrences[key] > 1:
        print("The repeated word \"" + str(key) + "\" has "
              + str(dict_occurrences[key]) + " occurrences in tuple")
