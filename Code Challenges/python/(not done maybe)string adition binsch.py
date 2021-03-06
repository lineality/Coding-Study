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
# String Addition
# Given two strings a, and b, both representing an integer, add them and return it in the same string representation.

# Bonus: can you implement the addition directly, instead of using eval or built-in big integers?

# Constraints`

# n ≤ 200 where n is the length of a
# m ≤ 200 where m is the length of b
# Example 1
# Input

# a = "12"
# b = "23"
# Output

# "35"
# Explanation

# 12 + 23 = 35


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


class Solution:
    def solve(self, string_1, string_2):
        return int(string_1) + int(string_2)


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input_1 = "1"
test_input_2 = "2"


run_test = Solution()
print("\nOutput   =", run_test.solve(test_input_1, test_input_2))

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