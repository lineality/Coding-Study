# https://binarysearch.com/
# detect voter fraud
#
# GGA 2020.11.05
#
# User Problem
# You have:
# You Need:
# You Must:
#
# Solution (Feature/Product)
# extract vote id numbers
#
#
#
# Edge cases:
#
# Input/Output Example:
#Detect Voter Fraud
# Given a two dimensional list of integers votes, where each list has two elements [candidate_id, voter_id], report whether any voter has voted more than once.

# Example 1
# Input

# votes = [
#     [3, 1],
#     [3, 0],
#     [3, 4],
#     [3, 3],
#     [3, 2]
# ]
# Output

# False

# Reflect On, Improvements, Comparisons with other Solutions:
#


class Solution:
    # find dupes in voter ID (from a 2d array (vanilla python))
    def solve(self, array_voting):

        # strip out 
        vote_id_only = [i[1] for i in array_voting]

        # see if set-length (no dupes) is different
        return len(vote_id_only) != len(set(vote_id_only))

class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution
run_test = Solution()
print("\nOutput   =", run_test.solve([
    [3, 1],
    [3, 0],
    [3, 4],
    [3, 3],
    [3, 2]
]))

run_test_2 = Solution_2()
print("\nOutput 2 =", run_test_2.solve("input"))


# Compare 2 Averaged runtimes
import time


# def compare_avg_times(iterations=1000000):

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
#         run_test.solve("input")

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
#         run_test_2.solve("input")

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