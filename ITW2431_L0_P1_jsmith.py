# Name: Jim Smith
# ITW 2431
# Lab 0 Prob. 1
# File name: ITW2431_L0_P1_jsmith.py
# MODIFIED: 1/10/22
# PURPOSE: Understand Nested Loop
# ASSUMPTIONS:

print("ITW 2431 Lab 0 Prob. 1 While Loop A")
a = 0
while a < 3:
  while True:
    print("X")
    break
  print("O")
  a = a + 1

print("\nITW 2431 Lab 0 Prob. 1 While Loop B")
a = 1
while a < 3:
  while a < 3:
    print("O")
    a = a + 1
    #a = a + 1


input('Please hit enter to close the application...')
