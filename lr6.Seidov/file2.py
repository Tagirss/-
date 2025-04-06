from file1 import *
def exponentiation(a,b):
    c = a
    for i in range(0,b-1):
        c = multiply(c,a)
    return c

def addition_and_multiply(a,b,c):
    return multiply(addition(a,b), c)

def addition_and_reminder(a,b):
    return division_reminder(addition(a,b), b)