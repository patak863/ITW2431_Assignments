# Name: Mike Patak
# ITW 2431
# Project 4 Prob. 1
# File name: ITW2431_P4_P1_mpatak.py
# MODIFIED: 2/13/22
# PURPOSE:  The program will create a dictionary to store the days of the
#           week as a key and a number as the value in a key value pair.
#           The program will then output the key/value pair first sorting
#           the output in ascending order and then sorting the output in
#           descending order.
# ASSUMPTIONS:  The program will use an existing dictionary for the data:
#               dictDays = {'Tuesday': 2,
#                           'Sunday': 7,
#                           'Monday': 1,
#                           'Thursday': 4,
#                           'Friday': 5,
#                           'Wednesday': 3,
#                           'Saturday': 6}
###########################################################################

dict_days = {'Tuesday': 2,
             'Sunday': 7,
             'Monday': 1,
             'Thursday': 4,
             'Friday': 5,
             'Wednesday': 3,
             'Saturday': 6}

list_items = list(dict_days.items())
# create a list to hold the sorted dictionary items
dict_sorted_items = list()

# setting up a bubble sort with two nested loops. The bubble will compare
# two values in a list and moving the smaller number to the right for a
# descending list (left to right: largest to smallest), and moving the
# smaller numbers to the left for a ascending list (left to right: smallest
# to largest).
def bubble_sort(str_direction):
    # the first loop will execute the length of the dictionary minus 1
    # loop1 gets the first item to compare
    for loop1 in range(len(dict_days) - 1):
        # loop2 gets the second item to compare
        for loop2 in range(loop1 + 1, len(dict_days)):
            # check if the dictionary item referenced using the loop1 value is
            # smaller than the dictionary item referenced using the loop2 value
            # if it is the items values will be swapped
            if str_direction == 'ascending':
                if list_items[loop1][1] > list_items[loop2][1]:
                    # assign the first items to a temp variable 'smaller_value'
                    larger_value = list_items[loop1]
                    # assign second item to first item place in dictionary
                    list_items[loop1] = list_items[loop2]
                    # assign the value in 'smaller_value' to second item place in dictionary
                    list_items[loop2] = larger_value
            elif str_direction == 'descending':
                if list_items[loop1][1] < list_items[loop2][1]:
                    # assign the first items to a temp variable 'smaller_value'
                    smaller_value = list_items[loop1]
                    # assign second item to first item place in dictionary
                    list_items[loop1] = list_items[loop2]
                    # assign the value in 'smaller_value' to second item place in dictionary
                    list_items[loop2] = smaller_value
    # use the dict() function with the sorted 'list_items' as a
    # parameter to create the dictionary dict_sortedItems
    dict_sorted = dict(list_items)
    return dict_sorted


print(dict_days)
dict_sorted_items = bubble_sort('ascending')
# loop through the dictionary of sorted items
print("Output in ascending order:")
for key in dict_sorted_items.keys():
    # print out the dictionary sorted in descending order
    print(str(key) +  " => " + str(dict_sorted_items[key]))

dict_sorted_items = bubble_sort('descending')
# loop through the dictionary of sorted items
print("Output in descending order:")
for key in dict_sorted_items.keys():
    # print out the dictionary sorted in descending order
    print(str(key) +  " => " + str(dict_sorted_items[key]))
