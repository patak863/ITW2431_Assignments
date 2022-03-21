# Name: Mike Patak
# ITW 2431
# Project 1 Problem 1
# File name: ITW2431_P1_P1_mpatak.py
# MODIFIED: 1/19/22
# PURPOSE:  The program will take 4 user inputs as variables. The 
#           program will calculate the total price paid by the customer.
#           The program will print out the price paid two different ways.
# ASSUMPTIONS:  The input will contain 4 elements: customer's name, 
#               price for the goods, number of goods purchased, and
#               name for the goods.
#########################################################################

import locale
# To use default settings, set locale to None or leave second argument blank.
locale.setlocale(locale.LC_ALL, '')

# Ask the user to input their name
str_custName = input("Please enter the customer's name: ")
# Ask the user for the price of the goods
float_price = float(input("Please enter the unit price for the goods: "))
# Ask the user for the number of goods purchased
int_numGoods = int(input("Please enter the number of goods purchased: "))
# Ask the user for the name of the goods 
str_goodsName = input("Please enter the name for the goods: ")

# calcualte the total cost of purchase
float_totalCost = float_price * int_numGoods

# print out with the total cost represented with one significant digit
print("The customer " + str_custName + " paid totally $" + str(float_totalCost) +
      " for " + str(int_numGoods) + " items of " + str_goodsName)
# print output with the total cast respresented with two significant digits
# using the 'currency' function from the 'locale' module
print("The customer " + str_custName + " paid totally " + locale.currency(float_totalCost) +
      " for " + str(int_numGoods) + " items of " + str_goodsName)
