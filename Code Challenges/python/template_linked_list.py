# GGA 2020.11.13
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
#
#    (Edge cases)
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#
####################
# Solution Code Here
####################

####################
# Solution Code Here
####################


class Solution:
    def solve(self, nums):
        pass


class Solution_2:
    def solve(self, nums):
        pass


###########################################
# Functions to Print Solution, Output, Time
###########################################

# Enter Your Input Here as a list
# will be turned into a linked-list
linked_list_items = [1, 2, 3]

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

    header = f"There are {node_number - 1} nodes.\n"

    return header + string_to_print


##################
# Run & See Output
##################
run_test = Solution()
# Run Solution
answer = run_test.solve(test_input)
# Print Output & Contents
print(print_linked_list(answer))

# Alt solution
print("Alt Solution:")
run_test_2 = Solution_2()
# Run Solution
answer_2 = run_test_2.solve(test_input)
# Print Output & Contents
print(print_linked_list(answer_2))


# Compare 2 Averaged runtimes
import time

# Adjust the number of iterations checked here
# (more will be slower, but 1,000,000 is good)
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