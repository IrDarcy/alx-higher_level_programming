#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical.
    """
for i in range(0, 90):
    if i % 10 > i / 10:
        if i != 89:
            print("{:02d}, ".format(i), end='')
        else:
            print("{:02d}".format(i))
