#!/usr/bin/python3
if __name__ == "__main__"
def element_at(my_list, idx):
    for i in my_list:
        if i == idx:
            return(my_list[i])
        elif idx < 0:
            return
        elif idx > len(my_list):
            return
