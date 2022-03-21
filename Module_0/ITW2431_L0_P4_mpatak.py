# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 4
# File name: ITW2431_L0_P4_mpatak.py
# MODIFIED: 1/13/22
# PURPOSE:  Understanding how changing the order of statements in a while loop
#           changes the output
# ASSUMPTIONS:

keep_going = True
a = 0
b = 0
while keep_going:
  print("O")
  a = a + 5
  b = b + 7
  if a + b >= 24:
    keep_going = False

print("end of 1")
print()

keep_going = True
a = 0
b = 0
while keep_going:
  print("O")
  if a + b >= 24:
    keep_going = False
  a = a + 5
  b = b + 7

print("end of 2")
print()

keep_going = True
a = 0
b = 0
while keep_going:
  print("O")
  a = a + 5
  b = b + 7
  if a + b > 24:
    keep_going = False

print("end of 3")
print()

keep_going = True
a = 0
b = 0
while keep_going:
  print("O")
  if a + b > 24:
    keep_going = False
  a = a + 5
  b = b + 7

print("end of 4")
