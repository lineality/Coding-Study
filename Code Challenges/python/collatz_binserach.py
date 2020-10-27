# https://binarysearch.com/

# Collatz sequence
# Given a positve integer n, find the length of its Collatz sequence. Collatz sequence is generated sequentially where

# n = n / 2 if n is even
# n = 3 * n + 1 if n is odd
# And the sequence ends if n = 1
# Example 1
# Input

# n = 11
# Output

# 15
# Explanation

# The Collatz sequence is: [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1] and its length is 15.


# GGA 2020.10.23
#
# User Problem
# You have: int
# You Need: length of Collatz sequence
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#


class Solution:
    def solve(self, n):

        counter = 1

        while n != 1:

            counter += 1

            if not n % 2:
                n = n / 2
                
            else:
                n = 3 * n + 1

            # # inspection
            # print("n", n)
            # print("counter", counter)

        return counter


Tom = Solution()
print(Tom.solve(11))
