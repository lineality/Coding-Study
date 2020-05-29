# (User) Problem
# We know / We have: a year
# We need / We don't have: what century that is
# We must: return integer
# name of function must be: centuryFromYear
#
# Solution (Product)
# look at last 2 digits (slice)
# plan for edge cases:
# edge case 1: if first century (from 0-100)
# edge case 2: if on the century year (200, 1200, etc)
# otherwise (asside from edge cases),
# the number will be (value preceeding last two digits)+1


def centuryFromYear(year):
    # edge case 1: if first century (from 0-100)
    if year < 101:
        return 1

    # edge case 2: if on the century year (x00)
    # get the last 2 characters: are they zeros?
    elif int(str(year)[-2:]) == 00:
        # return whatever preceeds the two zeros
        return int(str(year)[:-2])

    else:  # otherwise, the number will be (value preceeding last two digits)+1
        return (int(str(year)[:-2])) + 1
