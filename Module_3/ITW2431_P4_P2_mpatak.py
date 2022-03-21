# Name: Mike Patak
# ITW 2431
# Project 4 Prob. 2
# File name: ITW2431_P4_P2_mpatak.py
# MODIFIED: 2/13/22
# PURPOSE:  The program have an old sample dictionary {0: 10, 1: 20}. The
#           program will prompt the user for a number to be used for
#           adding numbers to the dictionary. The program will use a loop
#           to append the new key/value pairs to the dictionary. The
#           program will then print out the resulting dictionary after
#           each run that adds to the dictionary.
# ASSUMPTIONS:  The program will take input from the user for how many
#               name/value pairs to add to the dictionary.
###########################################################################

# create the dictionary 'dict_old'
dict_old = {0: 10, 1: 20}
# print out the old dictionary before any runs are added to it
print("Old dictionary is: " + str(dict_old))
# prompt the user for how many runs they want to add to dictionary
int_num_runs = int(input("How many runs do you want to add items"
                         "for dictionary: "))
# initialize variables int_key and int_value, which will be used to
# add new key/value pairs
int_key = 0
int_value = 0
# initialize the loop counter to 2, so that it will be the next key
int_counter = 2
# while will iterate the number of times equal
# to the value of int_num_runs
while int_counter < int_num_runs + 2:
    # assign int_key the value of int_counter
    int_key = int_counter
    # calculate the value of int_value
    int_value = int_key * 10 + 10
    # create the dictionary dict_temp using int_key for the key,
    # and int_value for the value
    dict_temp = {int_key: int_value}
    # update the old dictionary with the temp dictionary
    dict_old.update(dict_temp)
    # output the result of the run
    print("After the #" + str(int_counter - 1) + " run," +
          " the New dictionary is: " + str(dict_old))
    # increment the loop counter
    int_counter += 1
