# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         table = {}
#         for index,value in enumerate(nums):
#             if (target-value) in table:
#                 return [table[target-value], index]
#             else:
#                 table[value] = index


# leet code two sum
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# I/O Examples
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#

# loop through once and make hash table

values = [1, 2, 3, 4, 5]
target = 7

table = {}


def twosums(values, target):
    # make dictionary of
    # for index, number in enumerate(values):
    #     table[number] = index

    # both making table and checking table are combined...
    # Q: does this improve speed signficantly?
    #
    for index, number in enumerate(values):
        if (target - number) in table:
            return [table[target - number], index]

        # combining 
        else:
           table[number] = index


print(twosums(values, target))
