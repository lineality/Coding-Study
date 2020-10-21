# "Pigeonhole"
# You are given a list nums of length n + 1 picked from the range 1, 2, ..., n.
# By the pigeonhole principle, there must be a duplicate. Find and return it.
# There is guaranteed to be exactly one duplicate.


# the "difference" between two lists, if one number,
# is literally subtracting the sum of those sets.
class Solution:
    def solve(self, nums):  # input a list of ints including a dupe)

        # make a list with no dupes
        no_dupes_list = list(set(nums))

        # subtract the no-dupe list from the original
        return sum(nums) - sum(no_dupes_list)


Tom = Solution()
Tom.solve([1, 2, 3, 1])
