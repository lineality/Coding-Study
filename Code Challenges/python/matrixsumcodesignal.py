# (User's) Problem:
# We Have:
#     a 2d int array input
# We Need:
#     output which integers are not 'below' zero in columns
# We Must:
#     use function name:


# Solution (product):
#   Three goals:
#   1. convert list into a numpy array
#   2. iterate by column:
#      go through each number,
#      in each column, row by row...except...
#   3. Do not include any numbers in a column 'below' a zero
#     this is done by sequentially reading number down a column
#     and stopping (break) when you come to a zero,
#     then moving on to the next column

import numpy as np


def matrixElementsSum(input_list):

    # convert list into a numpy array
    input_list = np.array(input_list)

    # a list to store the answers
    # not_below_a_zero = []

    # total
    total = 0

    # use "shape" to get the range parameters
    for column in range(input_list.shape[1]):  # through columns
        # print("column",column)
        for row in range(input_list.shape[0]):  # throu}gh rows
            # print("row",row)
            # if you get to a zero, then STOP! (break)
            if input_list[row, column] == 0:
                break
            # add items to your answers list
            total += input_list[row, column]

    return total
