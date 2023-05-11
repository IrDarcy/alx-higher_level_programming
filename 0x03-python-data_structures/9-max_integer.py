#!/usr/bin/python3

def max_integer(my_list=[]):
    """function that returns biggest integer in list
    """

    list_length = len(my_list)

    if list_length == 0:
        return

    # sort the list in ascending order
    my_list.sort()

    return my_list[-1]
