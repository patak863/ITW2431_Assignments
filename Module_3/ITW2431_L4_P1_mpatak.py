# Name: Mike Patak
# ITW 2431
# Lab 4 Prob. 1
# File name: ITW2431_L4_P1_mpatak.py
# MODIFIED: 2/20/22
# PURPOSE:  The program will create a dictionary of name and birthday data.
#           The program will ask the user to enter the name of the person
#           whose birthday they want to find. If the birthday is found the
#           program will out the name and birthday. If the birthday is not
#           found the program will output an error message. After the user
#           is done searching for birthdays the first timer the program
#           will automatically added more names and birthdays to the
#           dictionary. The user will again be prompted for a name to
#           search for a birthday.
# ASSUMPTIONS:  The program will create a dictionary from data already
#               in the program.
############################################################################

# create initial dictionary of names and birthdays
dictBDays = {"Albert Einstein": "03/14/1879,",
             "Benjamin Franklin": "01/17/1706",
             "Ada Lovelace": "12/10/1815"}


def inquire_bday():
    # initialize bool_continue
    str_continue = ''
    while True:
        # print out the welcome message and list of known birthdays
        print("\nWelcome to the birthday query. We know the birthday of:\n")
        # for loop to iterate through the keys to print name list
        for key in dictBDays.keys():
            print("==> " + key)
        # prompt the user to enter name of person whose birthday to look up
        str_name = input("\nWho's birthday do you want to look up? ")
        # check if the name entered is in the dictionary keys
        if str_name in dictBDays.keys():
            # if name is in dictionary keys print out the birthday
            print("\n" + str_name + "'s birthday is " + dictBDays[str_name])
        else:
            # if the name entered is not in the dictionary print error message
            print("\nSorry, we don't have " + str_name + "'s birthday.")
        # ask the user if they want to continue
        str_continue = input("\nDo you want to continue (Y/N)?")
        # if the user enters 'n' or 'N' break out of the loop
        if str_continue == 'n' or str_continue == 'N':
            break  # this break will exit the while loop


# call the inquire birthday function to lookup birthday
inquire_bday()
# print message that more birthdays are being added
print("\nAdd more birthdays to the dictionary.")
# create a dictionary of new names and birthdays to add to dictBDays
dictUpdate = {"Charles Chaplin": "4/16/1889",
              "Franklin Delano Roosevelt": "1/30/1882"}
# use the dictionary update function to add new dictionary to dictBDays
dictBDays.update(dictUpdate)
# call the inquire birthday function to lookup birthday
inquire_bday()
