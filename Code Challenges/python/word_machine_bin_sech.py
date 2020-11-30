# https://binarysearch.com/
# GGA 2020.11.30

"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:
Word Machine
You are given a list of strings ops where each element is either:

A non-negative integer that should be pushed into a stack
"POP" meaning pop the top element in the stack
"DUP" meaning duplicate the top element in the stack
"+" meaning pop the top two and push the sum
"-" meaning pop the top two and push top - second
Return the top element in the stack after applying all operations. If there are any invalid operations, return -1.

Constraints

n ≤ 100,000 where n is the length of ops
Example 1
Input
ops = ["1", "5", "DUP", "3", "-"]

Output
-2

Explanation
Following the operations:

We push 1 into the stack: [1]
We push 5 into the stack: [1, 5]
We duplicate the top element: [1, 5, 5]
We push 3 into the stack: [1, 5, 5, 3]
We pop 3 and 5 and push their difference 3 - 5: [1, 5, -2]
We return the top element which is -2

Example 2
Input
ops = ["+"]

Output
-1

Explanation
There's no elements in the stack so this is invalid.

Solution (Feature/Product)

   (Edge cases)




Reflect On, Improvements, Comparisons with other Solutions:

I learned:
"""


class Solution:
    def solve(self, nums):
        pass


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "test"

run_test = Solution()
print("\nOutput   =", run_test.solve(test_input))

run_test_2 = Solution_2()
print("\nOutput 2 =", run_test_2.solve(test_input))


# Compare 2 Averaged runtimes
import time


def compare_avg_times(iterations=1000000):

    # store runtimes
    all_runtimes = 0

    # create class instance
    run_test = Solution()
    # create class instance
    run_test_2 = Solution_2()

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test.solve(test_input)

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # store the time for version 1
    time_1 = all_runtimes / iterations

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test_2.solve(test_input)

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # store the time for version 2
    time_2 = all_runtimes / iterations

    # return average runtime
    return print(
        "\nCompare Runtimes:",
        "\naverage time 1 = ",
        time_1,
        "\naverage time 2 = ",
        time_2,
    )


# print results
compare_avg_times()