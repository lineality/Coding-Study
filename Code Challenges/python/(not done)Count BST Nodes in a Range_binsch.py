# https://binarysearch.com/
# GGA 2020.12.04
"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:
Count BST Nodes in a Range
Given a binary search tree root, and integers lo and hi, return the count of all nodes in root whose values are between [lo, hi] (inclusive).

Constraints

n ≤ 100,000 where n is the number of nodes in root
Example 1
Input
Visualize Tree
root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]
lo = 5
hi = 10
Output
3
Explanation
Only 7, 8, 9 are between [5, 10].

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