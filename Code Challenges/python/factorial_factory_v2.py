# https://binarysearch.com/room/stack-smashers-4h7zTJbeDi
#
# by GGA 2020.10.20
#
# Problem (User's)
# Have: one number
# Need: factorial product of that number
# Must: return one integer

# Solution:
# For a recursive solution...
#
# First, establish your base case: when you cannot reduce any more, and so n=1
# (n =1 is the base case)
#
# For a recursive solution, you have a number of recursive steps equal to the input integer:
#
# For example, input = 4, has 4 steps
#
# n =  4
# n =  3
# n =  2
# Base Case! n =  1
# -> 24
#
# Once the base case is reached, each step (a stack of un-computed steps) unwinds
# and they are all computed at the end:
#
# Set up / creation order:
# 4th 3rd  2nd   1st
#
# # Compute order:
# 1st 2nd  3rd   4th
#
# n * (n * (n  * (n) ) )
# 1 * (2 * (3  * (4) ) )
# -> 24
#
# making a stack of N's to solve
# from 'top' to 'bottom'
#
# | 1 * |
# | 2 * |
# | 3 * |
# | 4 |
# | return |
#

# class Solution:
#     def solve(self, n):
#         # base case
#         if n == 1:

#             # # inspection
#             # print("Base Case! n = ", n)

#             return n

#         else:  # each time, multiply the number times solve(n - 1)

#             # # inspection
#             # print("n = ", n)

#             return n * self.solve(n - 1)

# tom = Solution()
# tom.solve(4)


class Solution:
    def solve(self, n):

        # set to 1 to avoid *0 error
        cumulative = 1

        # starts at 2, to avoid * zero error, and wasted 1*1 step)
        for i in range(2, n + 1):
            # # inspection
            # print(i)
            # print(cumulative)
            cumulative = cumulative * i

        return cumulative


tom = Solution()
tom.solve(4)
