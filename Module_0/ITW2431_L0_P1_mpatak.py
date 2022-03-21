# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 1
# File name: ITW2431_L0_P1_mpatak.py
# MODIFIED: 1/10/22
# PURPOSE: Print out the type of various values or calculations
# ASSUMPTIONS:

print("type(5) = " + str(type(5)))
print("type(\"abc\") = " + str(type("abc")))
print("type(True) = " + str(type(True)))
print("type(5.5) = " + str(type(5.5)))
print("type(12/27) = " + str(type(12/27)))
print("type(12//27) = " + str(type(12//27)))
print("type(2.0/1) = " + str(type(2.0/1)))
print("type(2.0//1) = " + str(type(2.0//1)))
print("type(12**3) = " + str(type(12 ** 3)))
print("type(12.0**3) = " + str(type(12.0**3)))
print("type(5 == \"5\") = " + str(type(5 == '5')))

a = str((-4 + abs(-5) // 2 ** 3) + 321 - ((64 // 16) % 4) ** 2)
print()
print("a = str((-4 + abs(-5) // 2 ** 3) + 321 - ((64 // 16) % 4) ** 2)")
print("type(a) = " + str(type(a)))
print("a = " + a)

a= str((-4 + abs(-5) / 2 ** 3) + 321 - ((64 / 16) % 4) ** 2)
print()
print("a= str((-4 + abs(-5) / 2 ** 3) + 321 - ((64 / 16) % 4) ** 2)")
print("type(a) = " + str(type(a)))
print("a = " + a)
