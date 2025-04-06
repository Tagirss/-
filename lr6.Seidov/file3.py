from file2 import *

def operation_one(a,b):
    return a-(multiply(a,b) + addition_and_reminder(a,b))

def operation_two(a,b):
    return multiply(addition_and_multiply(a,b), exponentiation(b,4))

def operation_three(a,b,c):
    return [addition(a,b), addition(a,c), addition(b,c)]