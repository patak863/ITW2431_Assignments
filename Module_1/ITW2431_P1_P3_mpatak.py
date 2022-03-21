# Name: Mike Patak
# ITW 2431
# Project 1 Problem 3
# File name: ITW2431_P1_P3_mpatak.py
# MODIFIED: 1/19/22
# PURPOSE:  The program will read an input file named 'ExamGrade.txt'.
#           Each line of the file contains a numerical grade. The program will
#           read each line and output the student and grade. After 
#           reading every grade the program will calcualte the average
#           of all grades.
# ASSUMPTIONS:  The input will only be the text file 'ExamGrade.txt'.
#########################################################################

# open the file handle for the data file
fhand = open('ExamGrade.txt')
# read all the lines in the file and place as string element in a list 'lines'
lines = fhand.readlines()

# initialize the variable for counting the lines of data
int_lineCount = 0
# initialize the variable for holding the sum of all the grades
int_gradeSum = 0

# the for loop will read each string element from 'lines'
for line in lines:
    # increment the int_lineCount to count how many lines in the file
    int_lineCount += 1
    # read the line for the grade and store as an 'int'
    int_gradeNum = int(line)
    # print the out for each student and their grade
    print("Student " + str(int_lineCount) + ": " + str(int_gradeNum))
    # add int_gradeNum to int_gradeSum to sum the grades as they are read
    int_gradeSum += int_gradeNum

# Calculate the average grade for the class
float_gradeAvg = float(round(int_gradeSum / int_lineCount, 2))
# Print out the average grade for the class
print("The average grade for the class is: " + str(float_gradeAvg))

# close the file
fhand.close()
