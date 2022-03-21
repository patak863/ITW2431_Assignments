# Name: Mike Patak
# ITW 2431
# Project 5 Prob. 1
# File name: ITW2431_P5_P1_mpatak.py
# MODIFIED: 2/20/22
# PURPOSE:  The program will read a data file for a students ID and his/her
#           grades for three exams. The students ID will be the key and
#           the three grades will be the value in a key/value pair. the
#           program will then output the average grade for each of the
#           three exams.
# ASSUMPTIONS:  The datafile 'studentGrade.txt' already exists.
############################################################################

# open the file handle for the data files
fhand_grades = open("studentGrade.txt")
# create the dictionary dict_grades
dict_grades = {}

# function will take a file handle and read the data from the file
# into a dictionary
def load_dict(fhand):
    for line in fhand:
        # use the split function to split the string into a list
        list_parsed_line = line.split()
        # initialize counter for while loop that will iterate through list
        int_counter = 0
        # assign the first element in the list, which is the student ID
        # to the key in the key/value pair
        str_key = list_parsed_line[0]
        # remove the first element from the list which is the student Id
        del list_parsed_line[0]
        # initialize a list that will be the value in the key/value pair
        list_value = list()
        # this while loop will execute for the number of elements in list
        # list and it will process as many grades as there are present
        while int_counter < len(list_parsed_line):
            list_value.append(int(list_parsed_line[int_counter]))
            int_counter += 1
            # create temporary dictionary with str_key and str_value
        dict_temp = {str_key: list_value}
        # update dict_grades with the dict_temp dictionary
        dict_grades.update(dict_temp)
            # increment int_counter
        int_counter += 1

# the function will take a dictionary as an argument and it will
# print out the grades for each student in the class
def print_grades(dict_print):
    # print the first line of the output
    print("The grades for the class are:")
    # for loop will iterate through each element in the dictionary
    for key in dict_print:
        # initialize loop counter
        int_counter = 0
        # initialize the output string that will hold the grades
        str_grade_output = ''
        # while loop will iterate through the dictionary values,
        # which in this instance is a list
        while int_counter < len(dict_print[key]):
            # assign list_temp the value associated with the key,
            # which in this instance is a list
            list_temp = dict_print[key]
            # each element in the list will be concatenated
            # to the grade output string
            str_grade_output += str(list_temp[int_counter]) + " "
            # increment the loop counter
            int_counter += 1
        # print the grades portion of the output
        print(key + " --> " + str_grade_output)


def print_avg_exam_grade(dict_avg):
    # initialize variables that will hold the total of
    # all the grades for each exam
    int_exam1_grades_total = 0
    int_exam2_grades_total = 0
    int_exam3_grades_total = 0
    # for loop will iterate through each element in the dictionary
    for key in dict_avg:
        # assign list_temp the value associated with the key,
        # which in this instance is a list
        list_temp = dict_avg[key]
        # initialize loop counter
        int_counter = 0
        # while loop will iterate through the list 'list_temp'
        while int_counter < len(list_temp):
            # if the int_counter is 0, then this is the first grade
            if int_counter == 0:
                int_exam1_grades_total += list_temp[int_counter]
            # if the int_counter is 1, then this is the second grade
            elif int_counter == 1:
                int_exam2_grades_total += list_temp[int_counter]
            # if the int_counter is 2, then this is the third grade
            elif int_counter == 2:
                int_exam3_grades_total += list_temp[int_counter]
            # increment loop counter
            int_counter += 1
    # print the average exam grade for each exam
    print("The average grade for exam 1 is: " +
          str(round(int_exam1_grades_total / len(dict_avg), 2)))
    print("The average grade for exam 2 is: " +
          str(round(int_exam2_grades_total / len(dict_avg), 2)))
    print("The average grade for exam 3 is: " +
          str(round(int_exam3_grades_total / len(dict_avg), 2)))

# call the load_dict function to load the dictionary
load_dict(fhand_grades)
# call the print_grades function to print out the grades for each student
print_grades(dict_grades)
# call the print_avg_exam_grade function to print the average for each exam
print_avg_exam_grade(dict_grades)
