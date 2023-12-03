#!/usr/bin/python3

if idx < 0:
    return
elif idx > len(my_list):
    return
else:
    for i in my_list:
        if i == idx:
            return(i)
