# Problem (User)
# We know / We have: a string
# We need / We don't have: first and last char
# We must / Requirements: function name: first_last
# no empty strings
#
# Solution (Product)
# 1. slice and make new string
# or
# 2. lambda


def first_last(character_string):
    # use 'slice's to get
    # the first and last character_string
    # then return those together
    first = character_string[0]
    last = character_string[-1]
    return first + last


# # lambda version: (works)
# first_last = lambda s: s[0] + s[-1]
