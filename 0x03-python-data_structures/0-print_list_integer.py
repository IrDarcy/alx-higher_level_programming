#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print integers function
    """
    if my_list:
        for integer in my_list:
            print("{:d}".format(integer))
