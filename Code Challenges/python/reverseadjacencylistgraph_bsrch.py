# for https://binarysearch.com/
# GGA 2021.01.01
# see https://www.tutorialspoint.com/program-to-reverse-the-directed-graph-in-python
"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:
Given a directed graph represented as an adjacency list, return its reverse so if an edge goes from A to B, it now goes from B to A.

Each list in the adjacency list should be sorted in ascending order.

Example 1
Input
Visualize
graph = [
    [1],
    [2],
    []
]
Output
Visualize
[
    [],
    [0],
    [1]
]
Explanation
In this example the nodes start off 0 -> 1 -> 2 and then become 0 <- 1 <- 2.
Solution (Feature/Product)

   (Edge cases)




Reflect On, Improvements, Comparisons with other Solutions:

I learned:


"""


# overall, this switches values for index-locations
class Solution:    
    def solve(self, graph):

        # list comprension:
        # pre-make an empty list-of-lists
        # that is the same size as the input
        answer_list = [[] for i in graph]

        # enumerate lists in the input list of lists
        for index, item_list in enumerate(graph):

            # for each actual item in the list 
            for number in item_list:

                # reversing what is the index and what is the content
                answer_list[number].append(index)

        return answer_list



class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = "test"

run_test_1 = Solution()
print("\nOutput of Solution 1 =", run_test_1.solve(test_input))

run_test_2 = Solution_2()
print("\nOutput of Solution 2 =", run_test_2.solve(test_input))


# Compare 2 Averaged runtimes
import time


def compare_avg_times(iterations=10000):

    # store runtimes
    all_runtimes = 0

    # create class instance
    run_test_1 = Solution()
    # create class instance
    run_test_2 = Solution_2()

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test_1.solve(test_input)

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