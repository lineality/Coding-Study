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
#     must be done in at least linear time? O(n)
#     so do it one pass
#
# Solution (Product)
# issue: too big or too small
# is the out of place number too big or too small?
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
    # edge caes: if already sorted and no dupes, return true
    if input_list == sorted(list(set(input_list))):
        return True

    # iterate through one time:
    # and check before and after any anomaly found:
    # anamoly = an item out of sequence
    for i in range(len(input_list) - 1):
        # look at previous: less than or = (repeating also not ok)
        if input_list[i] >= input_list[i + 1]:
            # conditionals for if out of place item is found
            # case 1: first item: remove first
            # case 2: last item: remove last
            # case 3: middle item: dropping each in tern
            #
            # case 1: first item: remove first
            if i == 0:
                input_list.pop(i)
            # case 2: last item: remove last
            elif i == len(input_list) - 1:
                input_list.pop(-1)
            # case 3: in middle so maybe too big or too small
            else:
                list_copy = input_list.copy()  # make a copy
                list_copy.pop(i)
                input_list.pop(i + 1)

            if input_list == sorted(list(set(input_list))) or list_copy == sorted(
                list(set(list_copy))
            ):
                return True

        else:  # otherwise, false:
            # more than one exception to being sorted
            return False
