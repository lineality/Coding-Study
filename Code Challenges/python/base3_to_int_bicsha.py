# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: string of int in base 3
# You Need: 10 int
# You Must:
#
# Input/Output Example:
# Base 3 to integer
# Given a string s representing a number in base 3 (consisting only of 0, 1, or 2), return its decimal integer equivalent.

# Example 1
# Input

# s = "10"
# Output

# 3
# Example 2
# Input

# s = "21"
# Output

# 7
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
# map


class Solution:
    def solve(self, base3_str):
        return int(base3_str, 3)


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "21"

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