# https://binarysearch.com/
#
# GGA 2020.10.23
#
# User Problem
# You have: two lists
#   
# You Need: sorted merged lists
#
# You Must: 
#
# Input/Output Example:
#
# Merging Two Sorted Lists
# Given two sorted lists of integers, merge them into one large sorted list.

# For example, given these two lists:

# lst0 = [5, 10, 15]
# lst1 = [3, 8, 9]
# Return [3, 5, 8, 9, 10, 15].

# Example 1
# Input

# lst0 = [5, 10, 15]
# lst1 = [3, 8, 9]
# Output

# [3, 5, 8, 9, 10, 15]

# Solution (Feature/Product)
#
# Edge cases:
# 
# Revision, Reflection, Future Versions, Action Items:
# 

class Solution_1:
    def solve(self, lst0, lst1):

        # iterate through one list
        for i in lst0:
            # add to the other
            lst1.append(i)
        
        # return sorted
        return sorted(lst1)

lst0 = [5, 10, 15]
lst1 = [3, 8, 9]
Tom = Solution_1()
print(Tom.solve(lst0, lst1))




class Solution_2:
    def solve(self, lst0, lst1):

        # return sorted
        return sorted([*lst0, *lst1])


lst0 = [5, 10, 15]
lst1 = [3, 8, 9]
Tom = Solution_2()
print(Tom.solve(lst0, lst1))


class Solution:
    def solve(self, lst0, lst1):
        lst0 += lst1

        # return sorted
        return sorted(lst0)



lst0 = [5, 10, 15]
lst1 = [3, 8, 9]
Tom = Solution()
print(Tom.solve(lst0, lst1))