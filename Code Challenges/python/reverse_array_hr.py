# GGA 2020.09.16
# https://www.hackerrank.com/challenges/arrays-ds/problem
#
# (User's) problem
# You Have: an array
# You Need: to reverse the array
# You Must:
#   input: array
#   output: array
#
# Solution (Product)
# 1. make new array of set size
# 2. iterate (original array) and populate (new array backwards)


def reverseArray(input_array):
    # 1. make new empty array
    # set length of new array to = old array
    new_array = [None] * len(input_array)

    counter = -1

    # 2. # 2. iterate (original array)
    # and populate (new array backwards)
    for i in input_array:
        new_array[counter] = i
        counter -= 1

    return new_array
