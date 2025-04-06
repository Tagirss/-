from file5 import *
from random import shuffle

def sum_of_lists(a,b,c,d,e,f):
    return reverse_list(a, b,c) + reverse_list(d,e,f)

def shuffle_list(a,b,c):
    lst = sort_descending(a,b,c)
    shuffle(lst)
    return lst

def sum_list_el(a,b,c):
    sum = 0
    lst = sort_descending(a,b,c)
    for i in range(0,len(lst)):
        sum += lst[i]
    return sum