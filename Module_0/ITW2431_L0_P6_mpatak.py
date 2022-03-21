# Name: Mike Patak
# ITW 2431
# Lab 0 Prob. 6
# File name: ITW2431_L0_P6_mpatak.py
# MODIFIED: 1/13/22
# PURPOSE: Understanding calling a function and getting return values
# ASSUMPTIONS:

def f(a):
    a = a + 5
    return a


b = 0
f(b)
print(b)
b = f(b)
print(b)

a =5
b=6

print()
print("Variable scope example")
print()
def max(a, b):
    if a > b:
        a=10
        return a
    else:
        return b


def max1(c, b):
    if c > b:
        a=10
        return c
    else:
        return b


print(max(7,6))
print(a)
print(max1(7,6))
print(a)
