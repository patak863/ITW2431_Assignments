# Name: Mike Patak
# ITW 2431
# Lab 11 Prob. 1
# File name: ITW2431_L11_P1_mpatak.py
# MODIFIED: 3/31/22
# PURPOSE:  Create a class named "PartyAnimal". The class will have two
#           methods, party() and display(). The program will create a
#           PartyAnimal object and the it will call the party() method to
#           add someone to the party and display their welcome message.
#           The program will also output a count of the current number of
#           guests at the party.
# ASSUMPTIONS:
###########################################################################

# define the class StringStuff
class PartyAnimal:
    # class constructor
    def __init__(self):
        self.totalNumber = 0
        self.name = ''

    # party() method to add someone and welcome them to the party
    def party(self, nam):
        # assign the input parameter to self.name
        self.name = nam
        # increment the variable keeping track of how many guests there are
        self.totalNumber += 1

    # display() method will print out the guest welcome message
    # display how many guests there are so far
    def display(self):
        # print out the welcome message
        print("Welcome to the party, " + self.name + " !\n" +
           "So far we have totally " + str(self.totalNumber) + " guests!\n")

# create an instance of the PartyAnimal class
p = PartyAnimal()
# call the party() method to add guest to party
p.party('Jon Snow')
# call the display() method to print guest welcome message
p.display()
# call the party() method to add guest to party
p.party('Daenerys Targaryen')
# call the display() method to print guest welcome message
p.display()
