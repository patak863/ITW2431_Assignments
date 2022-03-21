# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 3
# File name: ITW2431_L0_P3_mpatak.py
# MODIFIED: 1/13/22
# PURPOSE: Understanding while loops
# ASSUMPTIONS:

# commented out because it is infinite loop
#a = 5
#while a < 8:
#    print("X")
print("ERROR infinite loop")
print("end of 1")
print()

a = -1
while a < 3:
    print("X")
    a = a + 1

print("end of 2")
print()

a = 1
while a % 7 != 0:
    if a % 2 == 0:
        print("O")
    if a == 2:
        print("X")
    a = a + 1

print("end of 3")
print()
