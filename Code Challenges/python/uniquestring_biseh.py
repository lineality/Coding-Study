# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: a string
# You Need: TF are there non-unique characters
# You Must:
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
#
# A unique string
# Given a string s, determine whether it has all unique characters.

# Example 1
# Input

# s = "abcde"
# Output

# True
# Explanation

# All characters only occur once

# Example 2
# Input

# s = "aab"
# Output

# False

# Reflect On :
#


class Solution:
    def solve(self, string_input):
        # a set removes dupes
        # so compare original length
        # to set length
        return len(string_input) == len(set(string_input))


# Sample Print Solution & How Long to Run

import time

start = time.time()

run_test = Solution()
print("\nOutput =", run_test.solve("input"))

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
        run_test.solve("input")

        # stop clock, store that runtime
        all_runtimes += time.time() - start

    # return average runtime
    return all_runtimes / iterations


print("average time =", avg_time())