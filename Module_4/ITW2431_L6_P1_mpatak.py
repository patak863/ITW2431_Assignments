# Name: Mike Patak
# ITW 2431
# Lab 6 Prob. 1
# File name: ITW2431_L6_P1_mpatak.py
# MODIFIED: 2/24/22
# PURPOSE:  The program will create a tuple using course and instructor
#           data included in the program and print out the 'old tuple'.
#           The program will then update one of the course/instructor
#           tuple with a new course/instructor tuple and print out the
#           'updated tuple'.
# ASSUMPTIONS:  The data used by the program is hard coded in the program.
# NOTES:    The program does not convert the old tuple to a list to
#           do the updates. I wanted to do something different with the
#           fewest lines of code possible.
###########################################################################

tuple_old = ('Python II', 'Hao Zhang', 'Data Analytics', 'Cheryl Aasheim', 'IT issues', 'Jeff Kaleta')
print("The old tuple is: " + str(tuple_old))

# new tuple is created by slicing the first 2 elements that are not changing
# and adding the new third and forth elements and concatenating the rest of
# the old tuple.
tuple_updated = tuple_old[:2] + ('Network Security', 'Lei Chen') + tuple_old[4:]
print("The updated tuple is: " + str(tuple_updated))
