# https://binarysearch.com/
#
# GGA 2020.10.28
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
# Domino Placement
# You are given integers n and m representing a board
# of size n by m. You also have an unlimited number
# of 1 by 2 dominos.

# Return the maximum number of dominos that can be placed
# on the board such that they don't overlap and
# every domino lies entirely within the board.

# Example 1
# Input

# n = 2
# m = 2
# Output

# 2

# Solution (Feature/Product)
# since each domino covers two spaces
# half the number of spaces
# is the number of dominos
#
#
# Edge cases:
#
# Revision, Reflection, Future Versions, Action Items:
#


class Solution:
    def solve(self, n, m):
        # return half the number of spaces
        return (n * m) // 2


Tom = Solution()
Tom.solve("input")
