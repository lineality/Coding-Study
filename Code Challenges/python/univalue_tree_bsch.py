# https://binarysearch.com/
# GGA 2020.12.04
"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:
Univalue Tree
Given a binary tree root, return whether all values in the tree are the same.

Constraints

n ≤ 100,000 where n is the number of nodes in root
Example 1
Input
Visualize Tree
root =
2

2

2

2

2

Output
True
Explanation
Every node has the value 2

Example 2
Input
Visualize Tree
root =
2

2

2

9

Output
False
Explanation
There is a node with a value 9 while

Solution (Feature/Product)
    BFS Bredth first search,
    check to see if any change in value
    if so
    output false

    if no defv

   (Edge cases)




Reflect On, Improvements, Comparisons with other Solutions:

I learned:
"""

"""
#e.g.
if root is None:
    return True

if value is None:
    value = root.val

return root.val == value and self.solve(root.right, value) and self.solve(root.left, value)
"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        


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