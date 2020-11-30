# https://binarysearch.com/
#
# GGA 2020.11.13
#
# User Problem
# You Have: input string of a or b, b can change
# You Need: number of unique combinations
# You Must: 
#
# Input/Output Example:
#
# Unique ab Strings
# You are given a string s of "a" and "b"s. "a"s can stay "a" or turn into "b", but "b"s can't change.

# Return the number of unique strings that can be made.

# Constraints

# n ≤ 10,000 where n is the length of s
# Example 1
# Input

# s = "abba"
# Output

# 4

# Solution (Feature/Product)
# b is ignored
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
    def solve(self, string_input):
        count_a = string_input.count("a")
        return 2**count_a

class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "abba"

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