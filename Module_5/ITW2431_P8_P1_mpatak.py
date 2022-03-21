# Name: Mike Patak
# ITW 2431
# Project 8 Prob. 1
# File name: ITW2431_P8_P1_mpatak.py
# MODIFIED: 3/11/22
# PURPOSE:  The program will read a text file of student grade data. The
#           program will use regular expressions to parse the data and
#           load it into a dictionary. The program will then output the
#           contents of the dictionary, extract and output the list of
#           students, output the sum for exam 1, output the average for
#           exam 2, output each student and their class grade, the average
#           grade for all students in the class, and how many students
#           have a grade above the average.
# ASSUMPTIONS:  The data used by the program is in file 'student_data.txt'.
###########################################################################

# import the regular expression module
import re
# create a file handle to the data file
fhand_student_data = open("student_data.txt")
# create the dictionary to hold the student data
dict_student = dict()
# initialize variables
float_sum_exam1 = 0.0
float_avg_exam2 = 0.0
float_avg_class_grade = 0.0
int_above_avg = 0

# function to take the data from the file and load it into a dictionary
def load_dict(fhand):
    # create a local dictionary
    dict_local = {}
    # parse through the file one line at a time
    for line in fhand:
        # create list to hold the student grades
        list_temp = list()
        # regular expression to get the name for line of data
        list_name = re.findall(r'[a-zA-Z]+\s', line)
        # assign the name to string variable
        str_name = list_name[0].rstrip()
        # regular expression to get all of the student grades
        list_grades = re.findall(r'[0-9][0-9]\.?[0-9]?\s', line)
        # for loop to parse through the student grades
        for grade in list_grades:
            # assign the grade to the variable after stripping trailing whitespace
            float_grade = float(grade.rstrip())
            # append the grade to the temp list
            list_temp.append(float_grade)
        # update the local dictionary with the student name and grades
        dict_local = {**dict_local, **{str_name: list_temp}}
    # return the dictionary
    return dict_local

# function to calculate the sum of exam 1, takes the loaded
# dictionary as a parameter
def calc_sum_exam1(dict_data):
    # initialize local variable
    loc_float_sum_exam1 = 0.0
    # parse through the grades
    for grades in dict_data:
        # calculate the sum of all exam1 grades
        loc_float_sum_exam1 = round(loc_float_sum_exam1 + dict_data[grades][0], 2)
    # return the sum of exam1
    return loc_float_sum_exam1

# function to calculate the average grade for the whole class,
# takes the loaded dictionary as a parameter
def calc_class_avg(dict_data):
    # initialize local variables
    loc_float_sum_exam_total = 0.0
    loc_int_counter = 0.0
    # parse through the student grades
    for grades in dict_data:
        # increment the counter
        loc_int_counter += 1
        # calculate the sum of all exam1 grades
        loc_float_sum_exam_total = round(loc_float_sum_exam_total + dict_data[grades][0], 2)
        loc_float_sum_exam_total = round(loc_float_sum_exam_total + dict_data[grades][1], 2)
        loc_float_sum_exam_total = round(loc_float_sum_exam_total + dict_data[grades][2], 2)
        loc_float_sum_exam_total = round(loc_float_sum_exam_total + dict_data[grades][3], 2)
    # calculate th average grade for the class
    loc_float_avg_class_grade = round(loc_float_sum_exam_total / 4 / loc_int_counter, 2)
    # return the average grade for the class
    return loc_float_avg_class_grade

# function to calculate the average grade for exam 2,
# takes the loaded dictionary as a parameter
def calc_avg_exam2(dict_data):
    # initialize local variables
    loc_int_counter = 0
    loc_float_sum_exam2 = 0.0
    loc_float_avg_exam2 = 0.0
    # parse through the student grades
    for grades in dict_data:
        # increment the counter
        loc_int_counter += 1
        # calculate the sum of all exam 2 grades
        loc_float_sum_exam2 = round(loc_float_sum_exam2 + dict_data[grades][1], 2)
        # calculate the average of exam 2 grades
        loc_float_avg_exam2 = round(loc_float_sum_exam2 / loc_int_counter, 2)
    # return the average grade of exam 2
    return loc_float_avg_exam2

# function to calculate the student grade, takes
# loaded dictionary and average class grade as parameters
def calc_student_grade(dict_data, avg_grade):
    # initialize local variables
    loc_float_student_grade_total = 0.0
    loc_float_avg_student_grade = 0.0
    loc_int_above_avg_count = 0
    # parse through the student grade data
    for grades in dict_data:
        # calculate the sum of all exam grades
        loc_float_student_grade_total += dict_data[grades][0]
        loc_float_student_grade_total += dict_data[grades][1]
        loc_float_student_grade_total += dict_data[grades][2]
        loc_float_student_grade_total += dict_data[grades][3]
        # calculate the average grade for the student
        loc_float_avg_student_grade = round(loc_float_student_grade_total / 4, 2)
        # print out the students grade for the class
        print(str(grades) + "\'s grade for the class is " + str(loc_float_avg_student_grade))
        # check if students grade is above or below the average for the class
        if loc_float_avg_student_grade > avg_grade:
            # if the grade is above average increment the counter
            # for the number of students with grades above average
            loc_int_above_avg_count += 1
        # reset the values for the local variables
        loc_float_student_grade_total = 0.0
        loc_float_avg_student_grade = 0.0
    return loc_int_above_avg_count


# call the function to load the dictionary
# parameter is the file handle for the student data
dict_student = load_dict(fhand_student_data)
# print out the dictionary
print("\nThe result dictionary is " + str(dict_student) + "\n")
# call the function to get the list of students
# parameter is the loaded student dictionary
list_student = list(dict_student)
# print out the list of students
print("The students extracted from the file are: " + str(list_student) + "\n")
# call the function to calculate the sum of exam 1
# parameter is the loaded student dictionary
float_sum_exam1 = calc_sum_exam1(dict_student)
# print out the sum of exam 1
print("The sum for exam 1 is " + str(float_sum_exam1) + "\n")
# call the function to calculate the average of exam 2
# parameter is the loaded student dictionary
float_avg_exam2 = calc_avg_exam2(dict_student)
# print out the average of exam 2
print("The avg for exam 2 is " + str(float_avg_exam2) + "\n")
# call the function to calculate the average grade for the class
float_avg_class_grade = calc_class_avg(dict_student)
# call the function to calculate the students grade
# parameters are the loaded dictionary and the average class grade
# the output is the total number of students with grades above the average
int_above_avg = calc_student_grade(dict_student, float_avg_class_grade)
# print out the average for the class and
# the number of students with grades above average
print("\nThe average for the class is " + str(float_avg_class_grade) + "\n")
print("There are " + str(int_above_avg) + " students in the class whose grade " +
      "is above average for the class")
