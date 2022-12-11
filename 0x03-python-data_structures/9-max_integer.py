#!/usr/bin/python3

def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None

    else:
        for i in my_list:
            if my_list[0] < my_list[1]:
                temp = my_list[0]
                my_list[0] = my_list[1]
                my_list[1] = temp
        return my_list[0]
