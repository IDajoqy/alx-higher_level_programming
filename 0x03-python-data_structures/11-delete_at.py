#!/usr/bin/python3
def delet_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return my_list
