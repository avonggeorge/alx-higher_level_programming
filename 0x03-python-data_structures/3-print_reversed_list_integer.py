#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    x = my_list
    for i in x[::-1]:
        print("{}".format(i))
