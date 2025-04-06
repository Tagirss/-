from file4 import *

def reverse_list(a,b,c):
    return sorted_sum_list(a,b,c)[::-1]

def insert_element(a, b, index, value):
    lst = make_list_ab(a,b)
    lst.insert(index, value)
    return lst

def sort_descending(a,b,c):
    return sorted(make_list_abc(a,b,c), reverse=True)