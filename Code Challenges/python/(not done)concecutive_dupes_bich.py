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
#Consecutive Duplicates
# Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters such that there's no consecutive "X" and no consecutive "Y".

# Constraints

# n ≤ 100,000 where n is the length of s
# Example 1
# Input

# s = "YYYXYXX"
# Output

# "YXYX"
# Explanation

# One solution is to delete the first two "Y"s and the last "X".

# Solution (Feature/Product)
# 1. regex
# 2. iterate through and count blocks of x and y
# then return the sequence of those blocks

#    (Edge cases)
#
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#

# changing index and printing separately 


from collections import OrderedDict

class Solution:
    def solve(self, input_string):
    
        # turn into a list
        list(input_string)



        return
        #return "".join(OrderedDict.fromkeys(input_string))


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "YYYXYXX"

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