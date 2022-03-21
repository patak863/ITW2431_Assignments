# Name: Mike Patak
# ITW 2431
# Lab 2 Prob. 1
# File name: ITW2431_L2_P1_mpatak.py
# MODIFIED: 1/26/22
# PURPOSE:  The program will have two functions that will modify a list
#           elements. The first function 'chop' removes the first and
#           last elements from the list and returns the value of None.
#           The second function 'middle' will return a list the contains
#           all but the first and last elements. The output will show
#           the original list and the output of the 'chop' and 'middle'
#           functions on the list.
# ASSUMPTIONS: The list to be modified by 'chop' and 'middle' functions
#           will be a defined variable in the program.
#########################################################################

import copy

list_a = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh']
print("Initial list of elements: " + str(list(list_a)) + "\n")


def chop(list_chop):
    modList = copy.deepcopy(list_chop)
    modList.pop(0)
    modList.pop(len(modList) - 1)
    print("The chop(alist) function will remove the first and last element from list")
    print("chopList = " + str(list(modList)) + "\n")
    return None


def middle(list_middle):
    midList = copy.deepcopy(list_middle)
    midList = midList[1:len(midList) - 1]
    print("The middle(alist) function will print the list without the first and last element")
    print("midList = " + str(list(midList)))

# call the function chop(list_a)
chop(list_a)
# call the function middle(list_a)
middle(list_a)
