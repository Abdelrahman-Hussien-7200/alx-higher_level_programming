#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_l = my_list[:]
    for idx, i in enumerate(new_l):
        if i == search:
            new_l[idx] = replace
    return new_l
