#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i == idx:
            return(my_list[i])
        elif idx < 0:
            return
        elif idx > len(my_list):
            return

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
