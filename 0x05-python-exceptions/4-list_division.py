#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    abdo_list = []
    result_each_time = 0
    for i in range(list_length):
        try:
            result_each_time = my_list_1[i] / my_list_2[i]
        except TypeError:
            result_each_time = 0
            print("wrong type")
        except ZeroDivisionError:
            result_each_time = 0
            print("division by 0")
        except IndexError:
            result_each_time = 0
            print("out of range")
        finally:
            pass
        abdo_list.append(result_each_time)
    return abdo_list
