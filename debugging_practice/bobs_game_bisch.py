# https://binarysearch.com/
#
# GGA 2020.10.23
#
# User Problem
# You have: a list of numbers
#   
# You Need: the number of rounds in the game (int)
#
# You Must: return -1 if no victory
#
# Input/Output Example:
#
# Bob's Game
# Bob is playing a game with himself. He gives himself a list nums. 
# Each round, Bob chooses two elements of the list and replaces 
# them with one positive integer with the same sum as the numbers 
# he selected. Bob declares victory when all of the number in the 
# array are even.

# Return the minimum number of rounds Bob must make before he can 
# declare victory, or return -1 if Bob can never declare victory.

# Constraints

# 2 ≤ N ≤ 100,000 where N is the length of nums.
# 0 ≤ nums[i] ≤ 100,000
# Example 1
# Input

# nums = [1, 1, 3, 7, 6, 12]
# Output

# 2

# Solution (Feature/Product)
#
# count numbers are odd or even
# 
# if odd number of odd, return negative 1
# if even number of odds, return half that number
# 
# 
# 
# Edge cases:
# 
# Revision, Reflection, Future Versions, Action Items:
# 

class Solution:
    def solve(self, nums):

        # make a variable
        number_of_odd_numbers = 0

        # count the number of odd numbers in the list
        for i in nums:
            if i % 2 == 1:
                number_of_odd_numbers += 1
        
        # if odd number of odds, can't in, return -1
        if number_of_odd_numbers % 2 == 1:
            return -1

        else:
            return number_of_odd_numbers / 2

Tom = Solution()
print(Tom.solve([1, 1, 3, 7, 6, 12]))