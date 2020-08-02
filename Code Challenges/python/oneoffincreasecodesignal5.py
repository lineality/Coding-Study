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
#
# the approach here, which passes the overly-strict code-signal speed test
# is to slice the original array around each option and test that.


def almostIncreasingSequence(input_list):
    # edge caes: if already sorted and no dupes, return true
    if input_list == sorted(list(set(input_list))):
        return True

    else:
        # iterate through one time:
        # and check before and after any anomaly found:
        # anamoly = an item out of sequence
        for i in range(len(input_list) - 1):
            # look at previous: less than or = (repeating also not ok)
            if input_list[i] >= input_list[i + 1]:

                # issue: too big or too small: try removing each in turn
                # check if range excluding each in turn check-out
                # but use slices to check the range (as faster)

                # list without i
                mod1 = input_list[:i] + input_list[i + 1 :]
                # list without i+1
                mod2 = input_list[: i + 1] + input_list[i + 2 :]

                # check if either are correct
                if mod1 == sorted(list(set(mod1))) or mod2 == sorted(list(set(mod2))):
                    return True

                else:  # otherwise, false:
                    # more than one exception to being sorted
                    return False
