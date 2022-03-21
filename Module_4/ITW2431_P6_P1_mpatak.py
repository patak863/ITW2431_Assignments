# Name: Mike Patak
# ITW 2431
# Project 6 Prob. 1
# File name: ITW2431_P6_P1_mpatak.py
# MODIFIED: 2/27/22
# PURPOSE:  The program will use the 'input()' function to ask the
#           users to input their courses and professors this semester,
#           until the users input "done" to complete data entry. The
#           program will put the courses and professor names into a
#           tuple. The program will print out the data.
# ASSUMPTIONS: The program will take input via the command line that
#           will populate the tuple.
###########################################################################

# initialize string variables for course name and professor's name
str_courseName = ''
str_profName = ''
# initialize the lists and tuple for course name and professor's name
list_course_info = list()
tuple_course_info = tuple()

str_input = ''

while True:
    # Ask the user to input the course name
    str_courseName = input("Please enter the courses you are taking in this semester: ")
    # check to see if user entered 'done' for the course name
    if str_courseName == 'done':
        # if 'done' is entered break out of loop
        break
    else:
        # append the course name to the list holding course info
        list_course_info.append(str_courseName)
    # Ask the user to input the name of professor
    str_profName = input("Please enter the professor's name for the course: ")
    # append the professors name to the list holding course info
    list_course_info.append(str_profName)
    print()

# create a tuple of course info using the list_course_info loaded in the while loop
tuple_course_info = tuple(list_course_info)
# print the course info tuple
print(tuple_course_info)