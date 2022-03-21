# Name: Mike Patak
# ITW 2431
# Project 3 Prob. 1
# File name: ITW2431_P3_P1_mpatak.py
# MODIFIED: 2/6/22
# PURPOSE:  The program read to existing .txt files that have lists of
#           numbers in them. The program will find the numbers that are
#           overlapping, meaning the same number exists in both lists.
#           One .txt file has a list of all prime numbers under 1000,
#           and the other .txt file has a list of happy numbers up to
#           1000.The program will output a list of all the overlapping
#           numbers.
# ASSUMPTIONS:  The program will read two existing txt files, one
#               containing prime numbers (primenumbers.txt) under 1000
#               and happy numbers (happynumbers.txt) under 1000.
###########################################################################

# open the file handle for the data files
fhandPrime = open("primenumbers.txt")
fhandHappy = open("happynumbers.txt")


def listload(fhand):
    # Initialize list for holding numbers
    listnum = list()
    # for loop will read each line in the file and will exit when
    # there are no more lines to read
    for line in fhand:
        listnum.append(int(line.strip()))
    return listnum


# call the listload(fhand) passing fhandPrime as a parameter to load
# the file contents to a list
listPrime = listload(fhandPrime)
# call the listload(fhand) passing fhandHappy as a parameter to load
# the file contents to a list
listHappy = listload(fhandHappy)
# find the commone elements in both lists and save the result as a list
listOverlap = list(set(listPrime) & set(listHappy))
# sort the list of numbers from smallest to largest
listOverlap.sort()
# print the program output
print("The overlaping numbers in both files are: " + str(list(listOverlap)))
