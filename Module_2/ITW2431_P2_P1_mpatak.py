# Name: Mike Patak
# ITW 2431
# Project 6 Prob. 1
# File name: ITW2431_P6_P1_mpatak.py
# MODIFIED: 2/27/22
# PURPOSE:  The program will use the 'input()' function to ask the
#           users to input their courses and professors this semester,
#           until the users input "done" to complete data entry. The
#           program will put the courses and professor names into two
#           separate lists. The program will print out the data using
#           a for loop for each list.
# ASSUMPTIONS: The program will take input via the command line that
#           will populate the two lists.
###########################################################################

# initialize string variables for course name and professor's name
str_courseName = ''
str_profName = ''
# initialize the lists for course name and professor's name
list_courses = list()
list_professors = list()
# initialize while loop counter
int_count = 0

# while loop will read the input from command line until 'done' is
# entered for the course name. The while loop will take the course
# input and append to list_courses and the professors name input to
# list_professors
while True:
    # Ask the user to input the course name
    str_courseName = input("Please enter the courses you are taking in this semester: ")
    if str_courseName == 'done':
        break
    else:
        list_courses.append(str_courseName)
    # Ask the user to input the name of professor
    str_profName = input("Please enter the professor's name for the course: ")
    list_professors.append(str_profName)
    print()

# print out the list of courses and professors
print("The list for courses is " + str(list(list_courses)))
print("The list for professors is " + str(list(list_professors)))
print()

# initialize the strings for the formatted output
str_courseOutput = "The courses you are taking in this semester are: "
str_profOutput = "The professors for these courses are:\n"

# while loop will load the strings for formatted output
while int_count < len(list_courses):
    str_courseOutput += list_courses[int_count] + ", "
    str_profOutput += list_professors[int_count] + " ->\n"
    int_count +=1

# print the formatted output strings
print(str_courseOutput)
print(str_profOutput)
