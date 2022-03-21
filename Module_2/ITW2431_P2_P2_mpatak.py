# Name: Mike Patak
# ITW 2431
# Project 2 Prob. 2
# File name: ITW2431_P2_P2_mpatak.py
# MODIFIED: 1/26/22
# PURPOSE:  The program will prompt the user to enter a file name,
#           which the program will open and read it line by
#           line. The program will split the line into a list of words
#           using the 'split()'. Create a list by checking if a word is
#           already in the list, if it is not add it to list. The
#           program will output the created list in alphabetical order.
# ASSUMPTIONS:  The program will prompt the user for a file name and
#               for this problem we are looking for the 'romeo.txt' file.
###########################################################################

# prompt user for name of file
str_fileName = input("Enter file: ")
# open the file handle for the data file
fhand = open(str_fileName)

# initialize a list to add words to when parsing 'romeo.txt'
romeoList = []

# for loop will read each list in the file and will exit when
# there are no more lines to read
for line in fhand:
    # use the split function to split the string into a list
    parsedLine = line.split()
    # initialize the loop counter for the while loop
    # the will iterate through 'parsedList'
    int_counter = 0
    # the will loop will iterate through 'parsedList' elements.
    # If the element is not already in the 'romeoList' it will be
    # appended.
    while int_counter < len(parsedLine):
        # if the element is in 'romeoList' increment int_counter
        # and go to the top of wile loop
        if parsedLine[int_counter] in romeoList:
            int_counter += 1
            continue
        else:
            # if the element is not in 'romeoList' append it to 'romeoList'
            romeoList.append(parsedLine[int_counter])
        # increment int_counter
        int_counter += 1

# sort the 'romeoList' alphabetically
romeoList.sort()
# Print the output of the sorted 'romeoList'
print("romeoList: " + str(romeoList))
