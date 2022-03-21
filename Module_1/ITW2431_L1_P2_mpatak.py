# Name: Mike Patak
# ITW 2431
# Lab 1 Prob. 2
# File name: ITW2431_L1_P2_mpatak.py
# MODIFIED: 1/19/22
# PURPOSE:  The program will take as input a word. The program will
#           determine if the word entered is a palindrome or not.
# ASSUMPTIONS:  The input will only be a single word.
#########################################################################

# Ask the user to input a word
str_word = input("Please enter a word: ")


def is_palindrome(s):
    result = False
    # To reverse the string 's', s[::-1] slices the complete string from
    # the last character first (the -1 puts the slicing at the end of the
    # string) and read each character in the string in reverse by
    # decrementing the slice with -1 steps.
    str_revWord = s[::-1]
    # print the string 's' reversed
    print(str_revWord)
    # Check if string 's' and its reverse are equal.
    if s == str_revWord:
        # if 's' and 's[::-1]' are equal the result is True
        result = True
    # if 's' and 's[::-1]' are not equal the result is False
    return result

# call the function is_palindrome(str_word) passing the word from input() as parameter
palindromeResult = is_palindrome(str_word)
# check if result from is_palindrome() True or False
if palindromeResult == True:
    # print statement if is_palindrome()che result is True
    print("This word is a palindrome")
else:
    # print statement if is_palindrome() result is False
    print("This word is not a palindrome")
