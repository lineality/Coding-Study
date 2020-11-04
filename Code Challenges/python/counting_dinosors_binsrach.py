# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: two strings
# You Need: how many appearences of string 2 are in string 1
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
# Counting Dinosaurs
# You are given a string animals and another string dinosaurs. Every letter in animals represents a different type of animal and every unique character in dinosaurs represents a different dinosaur.

# Return the total number of dinosaurs in animals.

# Example 1
# Input

# animals = "abacabC"
# dinosaurs = "bC"
# Output

# 3
#
# Reflect On :
#

from collections import Counter


class Solution:
    def solve(self, string_1, string_2):

        # keep track of total items
        total = 0

        # using collections Counter: make a dict of instances in string 1
        dict_1 = Counter(string_1)

        # for each unique item in string_2
        # how many of those are in string_1
        # add those to total
        for i in set(string_2):
            total += dict_1[i]

        # return total
        return total


# Sample Print Solution & How Long to Run

import time

start = time.time()

run_test = Solution()
print("\nOutput =", run_test.solve("abc", "abd"))

print("Run Time = ", time.time() - start)

# Average Time:
import time

# takes the average runtime
def avg_time(iterations=1000000):

    # store runtimes
    all_runtimes = 0

    # create class instance
    run_test = Solution()

    # run the program X times
    # count the time
    for i in range(iterations):

        # start timer
        start = time.time()

        # run program
        run_test.solve("abc", "abd")

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # return average runtime
    return all_runtimes / iterations


print("average time =", avg_time())