# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: list of integers
# You Need: for sorted: which consecutive difference is greatest: vvalue
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
#
# Largest Gap
# Given a list of integers nums, return the largest difference of two consecutive integers in the sorted version of nums.

# Constraints

# n ≤ 100,000 where n is the length of nums
# Example 1
# Input

# nums = [4, 1, 2, 8, 9, 10]
# Output

# 4
# Reflect On, Improvements, Comparisons with other Solutions:
# using zip
# nums.sort()
# return max(b-a for a, b in zip(nums, nums[1:]))


class Solution:
    def solve(self, nums):
        # sort in place
        nums.sort()

        # max diff
        max_diff = 0

        # iterate, enumerate
        for index, value in enumerate(nums):

            # exclude last number
            if index != (len(nums) - 1):

                if max_diff < (nums[index + 1] - value):
                    max_diff = nums[index + 1] - value

        return max_diff


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution
run_test = Solution()
print("\nOutput   =", run_test.solve([4, 1, 2, 8, 9, 10]))

# run_test_2 = Solution_2()
# print("\nOutput 2 =", run_test_2.solve([4, 1, 2, 8, 9, 10]))


# # Compare 2 Averaged runtimes
# import time


# def compare_avg_times(iterations=1000000):

#     # store runtimes
#     all_runtimes = 0

#     # create class instance
#     run_test = Solution()
#     # create class instance
#     run_test_2 = Solution_2()

#     # run the program X times
#     # count the time
#     for i in range(iterations):

#         # start timer
#         start = time.time()

#         # run program
#         run_test.solve("input")

#         # stop clock, store that runtime
#         all_runtimes += time.time() - start

#     # store the time for version 1
#     time_1 = all_runtimes / iterations

#     # run the program X times
#     # count the time
#     for i in range(iterations):

#         # start timer
#         start = time.time()

#         # run program
#         run_test_2.solve("input")

#         # stop clock, store that runtime
#         all_runtimes += time.time() - start

#     # store the time for version 2
#     time_2 = all_runtimes / iterations

#     # return average runtime
#     return print(
#         "\nCompare Runtimes:",
#         "\naverage time 1 = ",
#         time_1,
#         "\naverage time 2 = ",
#         time_2,
#     )


# # print results
# compare_avg_times()