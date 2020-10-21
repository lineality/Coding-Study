# https://binarysearch.com/room/stack-smashers-4h7zTJbeDi

# Given a list of integers nums, a string op representing
# either "+", "-", "/", or "*", and an integer val, perform
# the operation on every number in nums with val and return
# the result.

# Note: "/" is integer division.


class Solution:
    def solve(self, nums, op, val):
        answer = [x + val for x in nums if op == "+"]
        answer = [x * val for x in nums if op == "*"]
        answer = [x // val for x in nums if op == "/"]
        answer = [x - val for x in nums if op == "-"]
        return answer


Tom = Solution()
Tom.solve([3, 1, 6], "-", 4)

# or


class Solution:
    def solve(self, nums, op, val):
        return (
            [x + val for x in nums if op == "+"]
            + [x * val for x in nums if op == "*"]
            + [x // val for x in nums if op == "/"]
            + [x - val for x in nums if op == "-"]
        )


Tom = Solution()
Tom.solve([3, 1, 6], "-", 4)
