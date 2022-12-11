#!/usr/bin/python3

def max_integer(my_list=[]):

    #Check if the list is empty

    if len(my_list) == 0:

        return None

    #Initialize the maximum integer

    max_int = my_list[0]

    #Loop through the list

    for num in my_list:

        #If the current number is greater than the maximum integer

        #Update the maximum integer

        if num > max_int:

            max_int = num

    #Return the maximum integer

    return max_int
