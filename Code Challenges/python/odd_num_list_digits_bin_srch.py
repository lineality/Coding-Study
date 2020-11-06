# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: list of numbers
# You Need: how many of those have an odd number of digits
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
#
# Odd number of digits
# Given a list of positive integers nums, return the number of integers that have odd number of digits.

# Example 1
# Input

# nums = [1, 800, 2, 10, 3]
# Output

# 4

# Reflect On, Improvements, Comparisons with other Solutions:
#


class Solution:
    def solve(self, nums):
        
        # make a counter
        counter = 0

        # iterate through list
        for i in nums:
            #check if odd
            if len(str(i)) % 2:
                counter += 1

        return counter

class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution
run_test = Solution()
print("\nOutput   =", run_test.solve([1, 800, 2, 10, 3]))

run_test_2 = Solution_2()
print("\nOutput 2 =", run_test_2.solve("input"))


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
        run_test.solve("input")

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
        run_test_2.solve("input")

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