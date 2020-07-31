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


# Strategy 2:
#     1. turn string into a list(array)
#     2. Make a compare_list which is the reverse order
#     3. return if those 2 lists are equal to each-other


def checkPalindrome(inputString):
    # make input a list
    input_as_list = list(inputString)

    # make a reverse list
    reverse_order = [None] * len(input_as_list)  # make blank array
    counter = 1
    for i in input_as_list:
        reverse_order[-counter] = i
        counter += 1

    # compare two lists
    return input_as_list == reverse_order
