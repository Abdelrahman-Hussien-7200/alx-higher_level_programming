#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    n = len(my_list)
    max_value = my_list[0]
    for i in range(n):
        if my_list[i] > max_value:
            max_value = my_list[i]
    return (max_value)
