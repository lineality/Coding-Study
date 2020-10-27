# https://binarysearch.com/

# GGA 2020.10.27
#
# User Problem
# You have: list of integers
# You Need: number of unique
# You Must: int
#
# Solution (Feature/Product)
#
# Edge cases:
# 



# Unique Integers in Sorted List Given a 
# list of sorted integers nums return 
# the number of unique integers in the 
# list.
# Contraints
# n ≤ 1,000,000 where n is the length 
# of nums Notes

# \mathcal{O}(n)O(n) is accepted but 
# \mathcal{O}(k\log{}n)O(klogn) is 
# encouraged. Example 1 Input

# nums = [2, 2, 2, 3, 4, 6, 6] Output

# 4

class Solution:
    def solve(self, nums):
        return len(set(nums))

Tom = Solution()
Tom.solve()