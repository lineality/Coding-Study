# https://binarysearch.com/
# linkedlist to int
#
# GGA 2020.11.05
#
# User Problem
# You have:
# You Need:
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
# Linked List to Integer
# Given a single linked list node, representing a binary number with most significant digits first, return it as an integer.

# Example 1
# Input

# node = 1 → 0 → 0
# Output

# 4

# Reflect On, Improvements, Comparisons with other Solutions:
#


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


# node = LLNode


class Solution:
    def solve(self, first_node):

        # store the LL as a string
        # toconvert that as base 2
        LL_as_string = ""

        node_pointer = first_node

        while node_pointer:
            # store the value
            LL_as_string += str(node_pointer.val)
            # advance
            node_pointer = node_pointer.next

        # convert str to binary to int
        # base 2
        return int(LL_as_string, 2)

class Solution_2:
    def solve(self, node):
        pass


# Sample Print Solution
run_test = Solution()
print("\nOutput   =", run_test.solve("input"))

run_test_2 = Solution_2()
print("\nOutput 2 =", run_test_2.solve("input"))


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
        run_test.solve("input")

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
        run_test_2.solve("input")

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