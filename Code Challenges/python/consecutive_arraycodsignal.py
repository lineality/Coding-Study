# makeArrayConsecutive2
# fill in the gaps:
# after array is sorted,
# how many additional values need to be added
# to make the array incrimented by 1?

# (User's) Problem
# We Have:
#     a array of int
# We Need:
#     fill in the gaps:
#     after array is sorted,
#     how many additional values need to be added
#     to make the array incrimented by 1?
# We Must:
#     return int
#
# Solution (Product)
#   1. sort the input_list
#   2. make a cumulative sum of the difference (subtraction)
#   between successive adjacent indices (between each item and the next)
#   Note: subtract 1, since no-needed-item is a difference of 1
#   e.g. between 3 and 5, one item is needed (5-3) = 2, 2-1 = 1


def makeArrayConsecutive2(input_list):
    cumulative_sum = 0

    # sort list
    input_list = sorted(input_list)

    # iterate and compare each to the next
    for i in range(0, (len(input_list) - 1)):
        # keep track of comparisons
        cumulative_sum += input_list[i + 1] - input_list[i] - 1

    return cumulative_sum
