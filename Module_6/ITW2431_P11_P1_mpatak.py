# Name: Mike Patak
# ITW 2431
# Project 11 Prob. 1
# File name: ITW2431_P11_P1_mpatak.py
# MODIFIED: 4/3/22
# PURPOSE:  Create a class named "bankBalance". The class will have two
#           methods, raise_rate() and cal_balance(). The program will
#           initialize two objects with an initial balance of $1000 and
#           $2000 dollars. The program will calculate a balance using the
#           initial balance and the number of years for interest to accrue.
#           The program will then raise the interest rate and calculate a new balance.
# ASSUMPTIONS:
###########################################################################

# define the class bankBalance
class bankBalance:
    # class constructor
    def __init__(self, name, bal, rate):
        # initialize instance variables
        self.name = name
        self.balance = bal
        self.rate = rate

    # class method to raise interest rate on account
    def raise_rate(self, rate):
        # assign new interest rate to self.rate
        self.rate = rate

    # class method to calculate the balance using an annual percentage rate
    def cal_balance(self, months, years):
        # calculate final balance
        final_balance = int(self.balance * (1 + (self.rate / months)) ** (months * years))
        print("The final balance for BankAccount \""+ self.name + "\" with initial balance of $" + str(self.balance) +
            " at the interest rate of " + str(self.rate) + " after " + str(years) + " is $" + str(final_balance))


print()
# create a bankBalance object 'a' for Jon Snow with an initial balance of $1000
# with an interest rate of 2% (.02)
a = bankBalance('Jon Snow', 1000, .02)
# create a bankBalance object 'b' for Sansa Stark with an initial balance of $2000
# with an interest rate of 2% (.02)
b = bankBalance('Sansa Stark', 2000, .02)

# call cal_balance() class method for Jon Snow with the number of months interest accrues as 12
# and the number of years as 2
a.cal_balance(12, 2)

# call cal_balance() class method for Sansa Stark with the number of months interest accrues as 12
# and the number of years as 3
b.cal_balance(12, 3)
# raise the interest rate for both Jon Snow and Sansa Stark accounts to 5% (.05)
a.raise_rate(.05)
b.raise_rate(.05)
print()
# call cal_balance() class method for Jon Snow with the number of months interest accrues as 12
# and the number of years as 2
a.cal_balance(12, 2)

# call cal_balance() class method for Sansa Stark with the number of months interest accrues as 12
# and the number of years as 3
b.cal_balance(12, 3)
print()
