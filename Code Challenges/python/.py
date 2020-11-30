# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have:
# You Need:
# You Must:
#
# Input/Output Example:
#
# Solution (Feature/Product)
#
#    (Edge cases)
#
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#


class Solution:
    def solve(self, nums):
        pass


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

# INPUT
# Put Your Input/Node-values HERE:
linked_list_items = [1, 2, 9, 4, 8]

# make a linked list
class Linked_List_Node_Class:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# make class
# test_input => This is the first node
test_input = Linked_List_Node_Class(None)

# for making list
place_holder_node = test_input

# make nodes
for i in linked_list_items:
    # fill the value of the current node
    place_holder_node.val = i

    # create the next node (blank to start with)
    place_holder_node.next = Linked_List_Node_Class(None)

    # set the placeholder to the next node
    place_holder_node = place_holder_node.next


# Get Basic Output Samples
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