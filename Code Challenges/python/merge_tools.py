# https://www.hackerrank.com/challenges/merge-the-tools
# GGA
# 
# Problem (User Problem)
#
# You Have:
#     Two inputs
#     1. string_input
#     2. "k" an integer (which is factor of len(string_intput))
# 
# You Need:
#    unique characters in each k-length segment of input
#
# You Must: 
#    name of function: "merge_the_tools"
#    new line for each output: e.g.
# an
# na
# te
#     edge case: if k = 1, print each letter as one line
# 
# Solution (Product / Feature for User)
#
# Steps:

# 1. iterate k times
# 2. slice k out of input
# K number of items starting at index
# 3. use OrderedDict to remove dupes
# 4. print on new line (or add new line)

from collections import OrderedDict 

# remove duplicates from 'k' segments
def merge_the_tools(input_string, k):

    # set your variable
    output_string = ''

    # edge case: k is 1
    if k == 1:
        for i in input_string:
            print(i)

    else:

        # 1. iterate k times
        for counter in range (1, k+1):

            # 2. slice k out of input
            item_string = input_string[ (counter-1)*k : (counter-1)*k + k ]

            # 3. use OrderedDict to remove dupes
            # 4. print on new line (or add new line)
            print( "".join(OrderedDict.fromkeys(item_string)) )


merge_the_tools("AABCAAADA", 3)
# merge_the_tools("aabb", 2)
# merge_the_tools("ABCdefGHI", 3)
