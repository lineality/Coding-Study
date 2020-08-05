# All The Longest
# Given an array of strings,
# return a new array containing all those elements
# that have the same largest-number of characters
# e.g.
# for ['I', 'am', 'cat', 'dog']
# output: ['cat', 'dog']

# User's (Problem)
# We Have:
#     a list of strings
# We Need:
#     longest(length) strings in the same order
# We Must:
#     name of function: allLongestStrings()
#
# Solution (Product):
#   goal: one pass, two steps (dictionaries are quick)
#
#   step 1: iterate through and
#   1.1  Keep track of longest length string you have observed
#   1.2  Create a dictionary that contains all those strings
#        Key = length of string, value = all strings of that length
#        note: check if value exists first, if not make one
#   step 2: return the dictionary value: key is longest length
#           value is all the items (in order) of that length


def allLongestStrings(input_list_of_stings):

    # keep track of length of longest string
    length_of_longest = 0

    # dictionary to store strings by length
    length_dict = {}

    # step 1: iterate through and
    # 1.1  Keep track of longest length string you have observed
    # 1.2  Create a dictionary that contains all those strings
    #      Key = length of string, value = all strings of that length
    for this_string in input_list_of_stings:
        # 1.1 check length and update length_of_longest
        if len(this_string) > length_of_longest:
            length_of_longest = len(this_string)

        # 1.2: first create key (and empty value list), then add value
        #      check if value exists first, if not make one
        if len(this_string) not in length_dict:
            length_dict[len(this_string)] = []

        length_dict[len(this_string)].extend([this_string])
        print(length_dict)

    # step 2: return the dictionary value: key is longest length
    #         value is all the items (in order) of that length
    return length_dict[length_of_longest]
