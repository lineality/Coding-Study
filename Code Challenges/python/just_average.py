# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: a list of numbers and k
# You Need: T/F one number can be removed from list for avg = k
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
# Just Average
# Given a list of integers nums and an integer k, return true if you can remove exactly one element from the list to make the average equal to exactly k.

# Constraints

# 2 ≤ n ≤ 1,000 where n is length of nums
# nums[i], k ≤ 1,000,000
# Example 1
# Input

# nums = [1, 2, 3, 10]
# k = 2
# Output

# True
#
# More optimal
# class Solution:
#     def solve(self, nums, k):
#         n = len(nums)
#         return sum(nums) - k * (n - 1) in nums


class Solution:
    def solve(self, list_of_numbers, k):

        new_k = len(list_of_numbers) - 1

        flag = False

        for i in list_of_numbers:
            if (sum(list_of_numbers) - i) / new_k == k:
                flag = True

        return flag


# Sample Print Solution & How Long to Run

import time

# start = time.time()

run_test = Solution()
print("\nOutput =", run_test.solve([1, 2, 3, 10], 2))

# print("Run Time = ", time.time() - start)

# Average Time:
import time

# takes the average runtime
def avg_time(iterations=1000000):

    # store runtimes
    all_runtimes = 0

    # create class instance
    run_test = Solution()

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test.solve([1, 2, 3, 10], 2)

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # return average runtime
    return all_runtimes / iterations


print("average time =", avg_time())
