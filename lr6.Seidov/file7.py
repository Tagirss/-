from file6 import *

def print_list_el(a,b,c,index):
    lst = shuffle_list(a,b,c)
    if len(lst) < index:
        index = 0
    print(lst[index])

def print_list(a,b,c,d,e,f):
    lst = sum_of_lists(a,b,c,d,e,f)
    for i in range(0, len(lst)):
        print(lst[i])

def print_sum_lst(a,b,c):
    print(f"Сумма элементов списка: {sum_list_el(a,b,c)}")
