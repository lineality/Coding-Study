# https://binarysearch.com/
#
# GGA 2020.10.27
#
# User Problem
# You have: a list of int
# You Need: sorted squares of each 
# You Must: resort the ouput
#
# Solution (Feature/Product)
#
# Edge cases:
# 
# Input/Output Example:
# Given a sorted list of integers, square the elements and 
# give the output in sorted order.

# Note: The integers can be 0 or negative.

# Example 1
# Input

# nums = [-9, -2, 0, 2, 3]
# Output

# [0, 4, 4, 9, 81]
# Example 2
# Input

# nums = [1, 2, 3, 4, 5]
# Output

# [1, 4, 9, 16, 25]


class Solution:
    def solve(self, nums):

        # iterate through the input list
        for i in range(0,len(nums)):

            # replace each item with it's own square
            nums[i] = nums[i]**2

        # return sorted version of that list
        return sorted(nums)


Tom = Solution()
Tom.solve([1, 2, 3, 4, 5])