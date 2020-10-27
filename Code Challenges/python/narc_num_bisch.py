# https://binarysearch.com/

# GGA 2020.10.27
#
# User Problem
# You have: int
# You Need: each digit ^ number of dig
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#

# input-ouput-example:
# Given an integer n, return whether it is equal to the 
# sum of its own digits raised to the power of the 
# number of digits.
# Example 1
# Input
# n = 153
# Output
# True


class Solution:
    def solve(self, nums):

        # get the length
        len_dig = len(str(nums))

        # set empty variable
        solution = 0

        # Make number into a list of numbers (strings)
        numlist_1 = list(str(nums))

        # Converst list of strings into list of integers
        numlist_2 = [int(i) for i in numlist_1]

        # add up the sums of each digit
        # raised to the power of the number of digits
        for i in numlist_2:
            solution += i ** len_dig
        
        # return if that sum is the original number
        return nums == solution


Tom = Solution()
Tom.solve(153)
