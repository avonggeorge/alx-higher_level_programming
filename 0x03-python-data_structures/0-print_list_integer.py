#!/usr/bin/python3
if __name__ == "__main__":

    def print_list_integer(my_list=[]):
        x = my_list
        for i in x:
            if isinstance(i, int):
                print("{}".format(i))
