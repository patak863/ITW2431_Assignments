# Name: Mike Patak
# ITW 2431
# Lab 3 Prob. 1
# File name: ITW2431_L3_P1_mpatak.py
# MODIFIED: 2/3/22
# PURPOSE:  The program will read the data from a file. The filename will be
#           input by the user. The program will check to see if a line that
#           starts with 'From', and if it does the program will split the
#           line into words using the split function. If the line starts with
#           'From' the second word will be printed out. The program will count
#           the number of lines that start with 'From' and print out the total.
# ASSUMPTIONS:  The file to be read as input exists already..
################################################################################

# prompt user for name of file
str_fileName = input("Enter file: ")
# open the file handle for the data file
fhand = open(str_fileName)

# Initialize the loop counter
int_counter = 0

# for loop will read each list in the file and will exit when
# there are no more lines to read
for line in fhand:
    # split the line into a list
    parsedList = line.split()
    # Check if the word 'From' is in the list
    if 'From' in parsedList:
        # print the second element in the list
        print(parsedList[1])
        # increment the loop counter
        int_counter += 1

# print the program output
print("There were " + str(int_counter) + " lines in the file with From as the first word")
