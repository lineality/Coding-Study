# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have:
# You Need:
# You Must:
#
# Solution (Feature/Product)
# make alphabet-flip dictionary
#
# Edge cases:
#
# Input/Output Example:
# Atbash cipher
# You are given a lowercase alphabet string text. Return a new string where every character in text is mapped to its reverse in the alphabet, so that a becomes z, b becomes y, c becomes x, and so on.

# Example 1
# Input

# text = "abcdef"
# Output

# "zyxwvu"

# Reflect On, Improvements, Comparisons with other Solutions:
#            # flip_dict[value] = abc[-(index + 1)]
#            flip_dict[value] = abc[~index]

# I learned:
#   zip, which is awsome
#   ~
#   simple list to string: "".join( [list_name] )


class Solution:
    def solve(self, text):
        # abc's
        abc = "abcdefghijklmnopqrstuvwxyz"

        # as list
        abc = list(abc)

        # make dictionary
        flip_dict = {}

        # iterate, enumerate
        for index, value in enumerate(abc):
            # make a flipped dictionary a -> z
            # flip_dict[value] = abc[-(index + 1)]
            flip_dict[value] = abc[~index]

        # return each item run through the flipped dictionary
        return "".join([flip_dict[i] for i in text])


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution
run_test = Solution()
print("\nOutput   =", run_test.solve("abcdef"))

# run_test_2 = Solution_2()
# print("\nOutput 2 =", run_test_2.solve("input"))


# # Compare 2 Averaged runtimes
# import time


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