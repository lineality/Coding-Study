# not working, not sure why (as parts work separately
# outside of function)
# (User's) Problem
# We have:
#     a string
# We need:
#     is that string a paindrome? yes/no
# We must:
#     boolean output
#     name of function is
#     checkPalindrome
# Solution (Product)


# Strategy 1:
#     turn string into a list(array)
#     Make a compare_list which is the reverse order of
#     the original list
#     compare the two, if they are the same: true, else false


def checkPalindrome(inputString):
    # make input a list
    input_as_list = list(inputString)
    # make a reverse list
    # (first make a copy)
    reverse_order = input_as_list
    # (this function has no input or output, it reverses in place)
    reverse_order.reverse()

    # compare two lists
    if input_as_list == reverse_order:
        return True
    else:
        return False
