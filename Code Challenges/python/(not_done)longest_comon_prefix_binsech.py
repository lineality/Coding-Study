# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You Have: list of strings
# You Need: longest common prefix
# You Must:
#
# Input/Output Example:
# Longest Common Prefix
# Given a list of lowercase alphabet strings words, return the longest common prefix.

# Example 1
# Input

# words = ["anthony", "ant", "antigravity"]
# Output

# "ant"
# Solution (Feature/Product)
#   look through each until a letter doesn't match
#    (Edge cases)
#   empty?
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#

test_input = ["test", "tent", "temble"]
boolean_result = all(word[i] > 3 for word in test_input)
print(boolean_result)

class Solution:
    def solve(self, input_words):
        # make something to output
        output_prefix = ""

        for i in range(len(input_words[0])):
            boolean_result = all(word > 3 for word[i] in input_words)

        print(boolean_result)


class Solution_2:
    def solve(self, words):
        pass


# Sample Print Solution

test_input = ["test", "tent", "temble"]

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