from file3 import *

def sorted_sum_list(a,b,c):
    return sorted(operation_three(a,b,c))

def make_list_ab(a,b):
    return [operation_one(a,b), operation_two(a,b)]

def make_list_abc(a,b,c):
    return [multiply(a,b), multiply(a,c), multiply(b,c)]