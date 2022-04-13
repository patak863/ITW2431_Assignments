# Name: Mike Patak
# ITW 2431
# Lab 10 Prob. 2
# File name: ITW2431_L10_P2_mpatak.py
# MODIFIED: 3/24/22
# PURPOSE:  Create a class named "bankBalance". The class will have two
#           methods, deposit() and withdraw(). The program will initialize
#           two objects with an initial balance of $1000 and $2000 dollars.
#           The program will make a deposit and a withdraw to each account
#           and print out the ending balance.
# ASSUMPTIONS:
###########################################################################

# define the class bankBalance
class bankBalance:
    # class constructor
    def __init__(self, num):
        # initialize instance variable
        self.balance = num

    # class method to add a deposit amount to the balance
    def deposit(self, num):
        # add the deposit amount to the balance
        self.balance += num
        # return the new balance value
        return self.balance

    # class method to subtract a withdraw amount from the balance
    def withdraw(self, num):
        # subtract the withdraw amount from the balance
        self.balance -= num
        # return the new balance value
        return self.balance

# initialize the variables for the deposit and withdraw amounts
int_deposit = 100
int_withdraw = 500
# create a bankBalance object 'a'
a = bankBalance(1000)
# call the bankBalance method deposit(num)
a.deposit(int_deposit)
# call the bankBalance method withdraw(num)
a.withdraw(int_withdraw)
# create a bankBalance object 'b'
b = bankBalance(2000)
# call the bankBalance method deposit(num)
b.deposit(int_deposit)
# call the bankBalance method withdraw(num)
b.withdraw(int_withdraw)
# print output for bankBalance objects 'a' and 'b'
print("The final balance for a is $" + str(a.balance))
print("The final balance for b is $" + str(b.balance))
