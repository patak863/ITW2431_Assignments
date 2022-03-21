# Name: Mike Patak
# ITW 2431
# Lab 7 Prob. 2
# File name: ITW2431_L7_P2_mpatak.py
# MODIFIED: 3/1/22
# PURPOSE:  The program will take a hardcoded dictionary and create a list of
#           tuples. The program will then sort the list in ascending order and
#           that list will be used to create a tuple using the sorted list.
#           The program will then output the sorted list. The program will then
#           sort the list in descending order and print out the sorted list.
# ASSUMPTIONS:
#           The program will use the dictionary:
#           dict = {'item4':65, 'item2':25, 'item5':234, 'item3': 31, 'item1':105}
##################################################################################

# create and load a dictionary
dict_pairs = {'item4':65, 'item2':25, 'item5':234, 'item3': 31, 'item1':105}
# create a list of tuples from dict_pairs using the items() function
list_of_tuples = list(dict_pairs.items())
# sor the list of tuples in ascending order
list_of_tuples.sort()
# create a tuple using the sorted list
tuple_sorted_list = tuple(list_of_tuples)
# initialize the loop counter
int_counter = 0
# print the first line of output for ascending order
print("The print result in ascending order:")
# while loop to iterate through the tuple
while int_counter < len(tuple_sorted_list):
    # using a string build a line of output
    str_output = tuple_sorted_list[int_counter][0] + " => " + \
                 str(tuple_sorted_list[int_counter][1])
    # print the output
    print(str_output)
    # increment the loop counter
    int_counter += 1

# sort the list of tuples in descending order
list_of_tuples.sort(reverse=True)
# create a tuple using the sorted list
tuple_sorted_list = tuple(list_of_tuples)
# reset the loop counter to 0 (zero) for new while loop
int_counter = 0
# print the first line of output for ascending order
print("The print result in descending order:")
# while loop to iterate through the tuple
while int_counter < len(tuple_sorted_list):
    # using a string build a line of output
    str_output = tuple_sorted_list[int_counter][0] + " => " + \
                 str(tuple_sorted_list[int_counter][1])
    # print the output
    print(str_output)
    # increment the loop counter
    int_counter += 1
