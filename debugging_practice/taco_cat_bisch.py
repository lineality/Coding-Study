# https://binarysearch.com/
#
# GGA 2020.10.23
#
# User Problem
# You have:
#
# You Need:
#
# You Must:
#
# Input/Output Example:
#
# Taco Cat
# Given a string s, return whether it is a palindrome.
# A palindrome is when the word is the same forwards
# and backwards.

# For example, "tacocat" is a palindrome.

# Example 1
# Input

# s = "racecar"
# Output

# True
# Example 2
# Input

# s = "evilolive"
# Output

# True

# Solution (Feature/Product)
#
# Edge cases:
#
# Revision, Reflection, Future Versions, Action Items:
#


class Solution:
    def solve(self, s):
        return s == s[::-1]

# Time Test
import time
start = time.time()
Demo_1 = Solution()
print("\nOutput = ", Demo_1.solve("tat"))
print ("Run Time = ", time.time()-start)

