# Name: Mike Patak
# ITW 2431
# Lab 9 Prob. 1
# File name: ITW2431_L9_P1_mpatak.py
# MODIFIED: 3/17/22
# PURPOSE:  The program will use a function to search a string and match
#           all the words that start with the letter 'a', and return the
#           immediately following words (the search will ignore
#           punctuation and digits). The program will then print out the
#           a list of the words that followed the letter 'a'.
# ASSUMPTIONS:
#           The data used by the program is hard coded in the program
#           as Str1 and Str2.
###########################################################################

# import the regular expression module
import re

# initialize test strings
Str1 = "Doesn't anybody stay in one place anymore. It would be so fine to see your face at my door."
Str2 = "Doesn't anybody-stay in one place anymore. It would be so fine to see your face at 2 my door."


# function to search match words the begin with the letter 'a' and return
# all the words that immediately follow.
def match_letter_a(str_data):
    # regular expression to match words starting with the letter 'a' and
    # catching the next word that is not a digit(s)
    x = re.findall(r'\ba\w+[-\s0-9.]*([a-zA-Z]+)', str_data)
    print(x)

# call the match_letter_a function for Str1 and Str2
match_letter_a(Str1)
match_letter_a(Str2)
