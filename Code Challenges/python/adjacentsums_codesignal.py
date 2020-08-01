# adjacent sums
#
# (User's) Problem
# We Have:
#    a list of integers
# We Need:
#    which adjacent sum is greatest
# We Must:
#    name of function: adjacentElementsProduct
#    output integer sum
#
# Solution (Product)
#    Two main parts:
#    1. mechanism to search
#      iterate through list, find sum of list[index]+list[index+1]
#      edge-case:
#    2. mechanism to record/find max number
#      a standard minimal solution is to use a
#      largest_sum variable that is updated
#
# edge cases:
#     Q: empty input? (nope)
#     if largest_product == 0:


def adjacentElementsProduct(input_list):
    # track largest_sum
    # note, this starting default value may be large than negative products
    largest_product = 0

    # iterate until penultimate index
    # i = counter_representing_an_index
    for i in range(len(input_list) - 1):
        # if new sum is biggest
        if input_list[i] * input_list[i + 1] > largest_product:
            # update largest_product
            largest_product = input_list[i] * input_list[i + 1]
        # edge case: products may be all negative
        if largest_product == 0:
            # update largest_product
            largest_product = input_list[i] * input_list[i + 1]

    return largest_product
