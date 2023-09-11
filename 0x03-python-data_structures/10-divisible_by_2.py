#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    new_list = []
    for i in range(n):
        if my_list[i] % 2 == 0:
            my_list.append(True)
        else:
            my_list.append(False)
    return (my_list)
