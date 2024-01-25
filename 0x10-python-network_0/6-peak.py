#!/usr/bin/python3
""" find a peak in a list of unsorted integers """


def recur(low, high, nums):
    """ recursively search """
    mid = (low + high) // 2
    if low == high:
        return nums[high]
    if nums[mid] < nums[mid + 1]:
        return(recur(mid + 1, high, nums))
    return(recur(low, mid, nums))


def find_peak(list_of_integers):
    """ find peak """
    if not list_of_integers:
        return
    return(recur(0, len(list_of_integers) - 1, list_of_integers))
