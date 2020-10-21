class Solution:
    def solve(self, nums, op, val):
        answer = [x + val for x in nums if op == "+"]
        answer = [x * val for x in nums if op == "*"]
        answer = [x // val for x in nums if op == "/"]
        answer = [x - val for x in nums if op == "-"]
        return answer


Tom = Solution()
Tom.solve([3, 1, 6], "-", 4)
