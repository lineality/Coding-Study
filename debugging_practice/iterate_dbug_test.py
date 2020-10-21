# Problem (User's)
# You Have: a list/array of int's
# You Need: sum of modified list: new_number = list[index]*(index-1)
# You Must: output as int
#
# Solution (Product/Feature)
#   keep at cumulative sum...
#   use enumarate
#
# Sample Expected input and ouput
# assuming [1, 2, 3, 4, 5]
# input     ouput
# 1 * -1    = -1
# 2 * 0     =  0
# 3 * 1     =  3
# 4 * 2     =  8
# 5 * 3     = 15
# ______________
# sum       = 25
#
# Testing & Debugging Notes

# default input
values = [1, 2, 3, 4, 5]


def mod_list_sum(input_list):
    total = 0

    for index, number in enumerate(input_list):
        number_mod = number * (index - 1)
        total += number_mod

    return total


# inspection
print(mod_list_sum(values))
