#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        for i in my_list:
            if idx is my_list[i]:
                return i
