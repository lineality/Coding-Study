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
#Recurring Character
# Given a string, return the index of the first recurring character in it. If there are no recurring characters, return -1.

# Example 1
# Input

# s = "abcda"
# Output

# 4
# Explanation

# The a at index 4 is the first recurring character.

# Example 2
# Input

# s = "abcde"
# Output

# -1
# Explanation

# No recurring characters in this string.

# Example 3
# Input

# s = "aaaaa"
# Output

# 1
# Explanation

# We want the first recurring character.

# Solution (Feature/Product)
#
#    (Edge cases)
#
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#

from collections import OrderedDict

class Solution:
    def solve(self, input_string):

        return OrderedDict.fromkeys(input_string)


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "test"

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