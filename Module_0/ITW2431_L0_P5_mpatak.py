# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 5
# File name: ITW2431_L0_P5_mpatak.py
# MODIFIED: 1/13/22
# PURPOSE: Understanding nested while loops
# ASSUMPTIONS:

a = 0
while a < 3:
  while True:
    print("X")
    break
  print("O")
  a = a + 1

print("end of 1")
print()

a = 1
while a < 3:
  while a < 3:
    print("O")
    a = a + 1

print("end of 2")
print()

a = 1
while a < 3:
  if a % 2 == 0:
    b = 1
    while b < 3:
      print("X")
      b = b + 1
  print("O")
  a = a + 1

print("end of 3")
print()

a = 1
while a < 3:
  b = 1
  while b < 3:
    if a == 2:
      print("X")
    print("O")
    b = b + 1
  print("O")
  a=a+1

print("end of 4")
