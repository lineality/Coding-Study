# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You Have:
# You Need:
# You Must:
#
# Input/Output Example:
# #Eliminate It!
# Given a string s, remove all “y” and “xz” in the string in one iteration.

# Example 1
# Input

# s = "xyxyxz"
# Output

# "xx"
# Example 2
# Input

# s = "xyz"
# Output

# "xz"
# Solution (Feature/Product)
# regex?
#    (Edge cases)
#
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#

import re


class Solution:
    def solve(self, text):

        # What you are trying to find
        pattern_1 = r"y"

        replace_with_this = ""

        # First remove
        text = re.sub(pattern_1, replace_with_this, text)

        pattern_2 = r"xz"

        # Second remove
        text = re.sub(pattern_2, replace_with_this, text)

        return text


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "xyxyxz"

run_test = Solution()
print("\nOutput   =", run_test.solve(test_input))

run_test_2 = Solution_2()
print("\nOutput 2 =", run_test_2.solve(test_input))


# Compare 2 Averaged runtimes
import time


def compare_avg_times(iterations=1000000):

    # store runtimes
    all_runtimes = 0

    # create class instance
    run_test = Solution()
    # create class instance
    run_test_2 = Solution_2()

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test.solve(test_input)

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # store the time for version 1
    time_1 = all_runtimes / iterations

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test_2.solve(test_input)

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # store the time for version 2
    time_2 = all_runtimes / iterations

    # return average runtime
    return print(
        "\nCompare Runtimes:",
        "\naverage time 1 = ",
        time_1,
        "\naverage time 2 = ",
        time_2,
    )


# print results
compare_avg_times()