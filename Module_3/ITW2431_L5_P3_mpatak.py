# Name: Mike Patak
# ITW 2431
# Lab 5 Prob. 3
# File name: ITW2431_P3_P1_mpatak.py
# MODIFIED: 2/17/22
# PURPOSE:  The program will print out the key/value pairs from a given
#           dictionary in descending order.
# ASSUMPTIONS:  The program will use the following dictionary:
#               dictItems = {'item1': 105,
#                            'item2': 25,
#                            'item3': 31,
#                            'item4': 65,
#                            'item5': 234}
############################################################################

# create the dictionary of items
dict_num_items = {'item1': 105, 'item2': 25, 'item3': 31, 'item4': 65, 'item5': 234}
# create a list using the items in the dictionary
list_items = list(dict_num_items.items())
# create a list to hold the sorted dictionary items
dict_sortedItems = list()

# setting up a bubble sort with two nested loops. The bubble will compare
# two numbers in a list and moving the smaller number to the right until
# it is the smallest and the right most number, or a smaller number is to
# the right of it.

# the first loop will execute the length of the dictionary minus 1
# loop1 gets the first item to compare
for loop1 in range(len(dict_num_items) - 1):
    # loop2 gets the second item to compare
    for loop2 in range(loop1 + 1, len(dict_num_items)):
        # check if the dictionary item referenced using the loop1 value is
        # smaller than the dictionary item referenced using the loop2 value
        # if it is the items values will be swapped
        if list_items[loop1][1] < list_items[loop2][1]:
            # assign the first items to a temp variable 'smallerValue'
            smallerValue = list_items[loop1]
            # assign second item to first item place in dictionary
            list_items[loop1] = list_items[loop2]
            # assign the value in 'smallerValue' to second item place in dictionary
            list_items[loop2] = smallerValue
    # use the dict() function with the sorted 'list_items' as a
    # parameter to create the dictionary dict_sortedItems
    dict_sortedItems = dict(list_items)

# loop through the dictionary of sorted items
for key in dict_sortedItems.keys():
    # print out the dictionary sorted in descending order
    print(str(key) +  " => " + str(dict_sortedItems[key]))

