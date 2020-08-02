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
# when you find a number out of sequence,
# is that number too big or too small?
# meaning: which number needs to be deleted?
# this is a fun logical question,
# but a simple approach of just removing and testing after every number
# may be for feasible in this case
# note: when checking each number, check on a copy of the list
# note: when using set() to check for dupes, it will unsort, so resort


def almostIncreasingSequence(int_list):

    # edge caes: if already sorted, and no dupes: return true
    if int_list == sorted(int_list) and int_list == sorted(list(set(int_list))):
        return True

    # check for just a duplicate
    if len(set(int_list)) == len(int_list) or len(set(int_list)) == len(int_list) - 1:
        return True

    # iterate through, and retest (like above) after removing each item
    for i in range(len(int_list)):
        # make sure you are using a copy
        test_list = int_list.copy()
        del test_list[i]

        if test_list == sorted(test_list) and test_list == sorted(list(set(test_list))):
            # if so, there was just one exception
            return True

    return False  # otherwise: false
