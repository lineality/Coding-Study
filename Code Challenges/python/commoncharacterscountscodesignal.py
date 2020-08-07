# Count Characters-in-common
# Given 2 strings, find the number of individual common characters
# e.g. aab vs. aac: they have TWO individual characters in common a and a

# User's (Problem)
# We Have:
#     Two strings
# We Need:
#     How many indivdual characters do those two strings have in common
# We Must:
#     name of function: commonCharacterCount()
#     return integer: number of strings in common
#     if none: return int 0
#
# Solution (Product):
#   The goal here is to try to keep the runtime complexity at O(n)
#   doing a single pass through each string,
#   thereafter only using dictionary-look-ups
#
#   Note: we will avoid using the build in functions to check
#   if characters are present, shared, etc., and redundant checks
#   will likely result in more than one search/sort iteration through
#   each string (which may be long). Once a dictionary of instances is made,
#   instead of laboriously going through the string over and over
#   we can use the very-optimized dictionary look up functions.
#
#   Step 1: user a helper function to make
#   two dictionaries of how many instances of
#   each character in each string.
#   string 1 instance dictiony and string 2 instance dictionary
#   key = character : value = number of dict_of_instances
#
#  Step 2:
# Compare characters "in common" and put totals in dict:
# if the character occurs in both dictionaries
# then take the lower number
# (the lower number is the number they have "in common")
#
# Step 3:
# add up all the numbers in the final_dict_of_instances
# finally, report that final tally.


# helper function: turn string into a dictionary of instances
def make_instance_dict(string_input):
    # make a dict
    dict_of_instances = {}

    # check if character already there:
    # if not already in dict: instance = 1
    for i in string_input:
        if i not in dict_of_instances:
            dict_of_instances[i] = 1
        # if already in dict: instance += 1
        else:
            dict_of_instances[i] += 1

    return dict_of_instances


# main function
def commonCharacterCount(str1, str2):

    # final tally (this is your final answer to output)
    final_tally = 0

    # make a final dictionary for both strings
    final_dict_of_instances = {}

    # Step 1:
    # for speedy processing
    # turn each input string into a dictionary of instances
    # using the helper function
    string1_dict = make_instance_dict(str1)
    string2_dict = make_instance_dict(str2)

    # Step 2:
    # Compare characters "in common" and put totals in dict:
    # if the character occurs in both dictionaries
    # then take the lower number
    # (the lower number is the number they have "in common")
    for char in string1_dict:
        # if in both
        if char in string1_dict and char in string2_dict:
            # take lower: if 1 is lower use it, else use 2
            if string1_dict[char] < string2_dict[char]:
                final_dict_of_instances[char] = string1_dict[char]
            else:
                final_dict_of_instances[char] = string2_dict[char]

    # Step 3:
    # add up all the numbers in the final_dict_of_instances
    for instances in final_dict_of_instances.values():
        final_tally += instances

    return final_tally
