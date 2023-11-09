#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Create a set from the list to remove duplicates
    unique_set = set(my_list)
    
    # Sum all elements in the set and return the result
    return sum(unique_set)
