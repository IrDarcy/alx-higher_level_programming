#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list
    """

    list_length = len(my_list)
    new_list = []

    for num in range(list_length):
        if my_list[num] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
