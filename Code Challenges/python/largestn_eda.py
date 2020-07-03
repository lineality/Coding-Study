# (User's) problem
# We have: a list of numbers
# We need: the largest number
# We must: function name (findLargestNum)
#
# Solution(Product):
# use max()
#
# Note: this will work for lists, tuples, and dictionary keys


# normal function:
def findLargestNum(list_of_numbers):
    # return the largest item in the input list etc
    return max(list_of_numbers)


# lambda version:
findLargestNum = lambda x: max(x)
