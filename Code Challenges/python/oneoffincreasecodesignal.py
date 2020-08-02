# almostIncreasingSequence or "too big or too small"
# is there one exception to the list being sorted? (with no repeats)
# including being already sorted

# (User's) Problem
# We Have:
#     list of int
# We Need:
#     Is there one exception to the list being sorted? yes/no
# We Must:
#     return boolean: true false
#     use function name: almostIncreasingSequence()
#
# Solution (Product)
# issue: too big or too small
# is the out of place number too big or too small?
# (alternate test: try it both ways)
#
# edge case: if already sorted: true
# iterate through input_list
# compare each item to previous (so starting with index 1)
# if i+1 is smaller, remove that item from list and
# then recheck if list is now sorted
# if so, the list was only one-off from being sorted
# use set to remove duplicates
#
# issue: too big or too small
# because when there is an anomology it isn't clear which number to remove...


# if first number, it's too big
# if last number, it's too small
# if in middle: ?
# if backwards iterate is smaller than or equal to next 2 numbers
# then remove -i
# else remove -(i+1)


def almostIncreasingSequence(input_list):
    # edge caes: if already sorted, return true
    if input_list == sorted(input_list) and input_list == list(set(input_list)):
        return True

    # iterate through backwards, comparing each item to previous:
    # look for an item out of sequence
    for i in range(1, len(input_list)):
        # look at previous: less than or = (repeating also not ok)
        if input_list[-i] <= input_list[-(i + 1)]:
            print(i)
            # conditionals for if out of place item is found
            if i == len(input_list):  # if last item
                input_list.pop(-i)
            elif input_list[-i] <= input_list[-(i + 2)]:
                input_list.pop(-i)
            else:
                # drop if found
                input_list.pop(-(i + 1))
            # recheck to see if sorted and no duplicates
            if input_list == sorted(input_list) and input_list == list(set(input_list)):
                # if so, there was just one exception
                return True

            else:  # otherwise, false:
                # more than one exception to being sorted
                return False
