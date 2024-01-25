#!/usr/bin/python3
""" find a peak in a list of unsorted integers """


def recursivesearch(low, high, nums):
    mid = (low + high) // 2
    if low == high:
        return nums[high]
    if nums[mid] < nums[mid + 1]:
        return(recursivesearch(mid + 1, high, nums))
    return(recursivesearch(low, mid, nums))

def find_peak(list_of_integers):
    if not list_of_integers:
        return
    return(recursivesearch(0, len(list_of_integers) - 1, list_of_integers))
