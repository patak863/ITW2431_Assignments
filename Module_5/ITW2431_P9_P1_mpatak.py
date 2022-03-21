# Name: Mike Patak
# ITW 2431
# Project 9 Prob. 1
# File name: ITW2431_P9_P1_mpatak.py
# MODIFIED: 3/18/22
# PURPOSE:  The program will read a data file and load the data into a
#           dictionary and output the dictionary contents. The program
#           will then retrieve the number of key:value pairs and output
#           the number. The program will then prompt the user for input
#           of a providers name and if the name is in the dictionary
#           the program will output the providers address and phone
#           number. If the providers name is not found the user will be
#           prompted to correct the name and enter again.
# ASSUMPTIONS:  The data used by the program is in file 'ClinicInfo.txt'.
###########################################################################

# import the regular expression module
import re
# create a file handle to the data file
fhand = open("ClinicInfo.txt")
# initialize the dictionary to hold provider information
dict_provider_info = dict()

# function containing a regular expression to get the providers name
def get_provider_name(str_data):
    # regular expression to get the providers name
    x = re.findall('[a-zA-z]+:\s([a-zA-Z &:\-\']+)', str_data)
    # strip whitespace
    loc_str_name = x[0].strip()
    # return the providers name
    return loc_str_name

# function containing a regular expression to get the providers address
def get_provider_address(str_data):
    # regular expression to get the providers address
    x = re.findall('[mi -]([a-zA-Z0-9 ,]+)', str_data)
    # strip whitespace
    loc_str_address = x[1].lstrip()
    # return the address
    return loc_str_address

# function containing a regular expression to get the providers phone number
def get_provider_phone(str_data):
    # regular expression to get the providers phone number
    x = re.findall('\w{3}-\w{3}-\w{4}', str_data)
    # strip whitespace
    loc_str_phone = x[0].strip()
    # return the phone number
    return loc_str_phone

# loop through all the lines of data in the file
for line in fhand:
    # strip whitespace
    line.strip()
    # check if the line is blank/empty
    if not line.strip():
        # if the line was empty continue to read the next line of data
        continue
    else:
        # if line was not empty check if next line contains the clinic name
        str_name_chk = re.search(r'Clinic Name:', line)
        if str_name_chk:
            # if clinic name line of data get the providers name
            str_provider_name = get_provider_name(line)
            # continue to read the next line of data
            continue
        # check if line of data contains the address
        str_address_chk = re.search(r'mi -', line)
        if str_address_chk:
            # if address line of data get the providers address
            str_provider_address = get_provider_address(line)
            # continue to read the next line of data
            continue
        # check if line of data contains the phone number
        str_phone_chk = re.search('\w{3}-\w{3}-\w{4}', line)
        if str_phone_chk:
            # if phone number line of data get the providers phone number
            str_provider_phone = get_provider_phone(line)
            # create a temporary list with address and phone number
            list_temp = [str_provider_address, str_provider_phone]
            # add a new dictionary key:value pair to provider dictionary
            dict_provider_info = {**dict_provider_info, **{str_provider_name: list_temp}}
            # continue to read the next line of data
            continue

# output the provider dictionary contents
print()
print(dict_provider_info)
# output the number of key:value pairs in dictionary
print("\nThe total number for key:value pairs in the dictionary is: " +
       str(len(dict_provider_info)))

# prompt the user for the providers name
while True:
    str_input_name = input("\nPlease input the query clinic provider's name: ")
    # check in name entered is in provider dictionary
    if str_input_name in dict_provider_info:
        # is name is found get the values and assign to list
        list_provider_data = dict_provider_info[str_input_name]
        # output the providers address
        print(str_input_name + " => " + str(list_provider_data[0]))
        # output the providers phone number
        print(str_input_name + " => " + str(list_provider_data[1]))
        # break out of the loop
        break
    else:
        # if name is not found prompt the user to correct name
        print("\nPlease correct the provider's name and try again")

