# https://binarysearch.com/
#
# GGA 2020.11.12
#
# User Problem
# You have: a singly linked list
# You Need: a reduced list, where each node skips ahead according
#           to the value of that node, so value 3 skips ahead 3
# You Must:
#
# Input/Output Example:
# Linked List Jumps
# You are given a singly linked list node containing positive integers.
# Return the same linked list where every node's next points to the node
# val nodes ahead. If there's no such node, next should point to null.

# Connstraints
# n ≤ 100,000 where n is the number of nodes in node
# Example 1

# Input
# node = 1 → 2 → 9 → 4 → 8

# Output
# 1 → 2 → 4

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

# class LLNode:
#   def __init__(self, val, next=None):
#        self.val = val
#        self.next = next


class Solution:
    def solve(self, head_node):

        # Note for exporting at the end, export the head node

        # for use
        this_node = head_node

        # until there is no 'next' node
        while this_node is not None:

            # set placeholder to be 'this node'
            # it will then jump ahead of 'this node'
            skip_ahead_pointer = this_node

            # this many skiped-node steps ahead
            steps_count_down = this_node.val

            # move the 'next' node pointer skip_ahead_pointer ahead
            # the number of times equal to the value of this_node
            # e.g. val=2, move ahead 2 nodes! (if there are two nodes to move ahead)
            while steps_count_down > 0 and skip_ahead_pointer is not None:

                skip_ahead_pointer = skip_ahead_pointer.next

                # # inspection:
                # print("this_node", this_node.val)
                # print("skip ahead pointer", skip_ahead_pointer.val)

                # decriment steps
                steps_count_down -= 1

            # set the 'next' value in the linked list
            # to this skipped-ahead value you caluculated above
            this_node.next = skip_ahead_pointer

            # increment to next (skipping ahead) Node
            this_node = this_node.next

        return head_node


class Solution_2:
    def solve(self, nums):
        pass


###########################################
# Functions to Print Solution, Output, Time
###########################################

# Enter Your Input Here as a list
# will be turned into a linked-list
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


def print_linked_list(head_node):

    node_number = 1
    this_node = head_node
    string_to_print = ""
    header = ""

    while this_node is not None:
        string_to_print += f"Node {node_number} = {this_node.val}\n"
        this_node = this_node.next
        node_number += 1

    header = f"There are {node_number - 1} nodes\n"

    return header + string_to_print


##################
# Run & See Output
##################
run_test = Solution()
# Run Solution
answer = run_test.solve(test_input)
# Print Output & Contents
print(print_linked_list(answer))

# run_test_2 = Solution_2()
# print("\nOutput 2 =", run_test_2.solve(test_input))

# # Get Run-time Tests
# # Compare 2 Averaged runtimes
# import time


# def compare_avg_times(iterations=1000):

#     # store runtimes
#     all_runtimes = 0

#     # create class instance
#     run_test = Solution()
#     # create class instance
#     run_test_2 = Solution_2()

#     # run the program X times
#     # count the time
#     for i in range(iterations):

#         # start timer
#         start = time.time()

#         # run program
#         run_test.solve(test_input)

#         # stop clock, store that runtime
#         all_runtimes += time.time() - start

#     # store the time for version 1
#     time_1 = all_runtimes / iterations

#     # run the program X times
#     # count the time
#     for i in range(iterations):

#         # start timer
#         start = time.time()

#         # run program
#         run_test_2.solve(test_input)

#         # stop clock, store that runtime
#         all_runtimes += time.time() - start

#     # store the time for version 2
#     time_2 = all_runtimes / iterations

#     # return average runtime
#     return print(
#         "\nCompare Runtimes:",
#         "\naverage time 1 = ",
#         time_1,
#         "\naverage time 2 = ",
#         time_2,
#     )


# # print results
# compare_avg_times()