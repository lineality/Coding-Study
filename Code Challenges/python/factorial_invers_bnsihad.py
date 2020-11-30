# https://binarysearch.com/
#
# GGA 2020.11.04
#
# User Problem
# You have: a number
# You Need: inverse factorial
# You Must: no answer -1
#
# Input/Output Example:
#Inverse Factorial
# The factorial of a number n is defined as 
# n! = n * (n - 1) * (n - 2) * ... * 1.

# Given a positive integer a, return n such that n! = a. 
# If there is no integer n that is a factorial, then return -1.

# Constraints

# n < 2 ** 31
# Example 1
# Input

# a = 6
# Output

# 3
#
# Solution (Feature/Product)
#  divide by increasing integers from 2, until you hit a prime
# 
# 
#    (Edge cases)
#    no answer -1
#
#
#
# Reflect On, Improvements, Comparisons with other Solutions:
#
# I learned:
#

class Solution:
    def solve(self, num):

        divid_by_this = 2

        while num > 1:

            # set input to new value
            num /= divid_by_this

            # increment 
            divid_by_this += 1

            # if the number is a prime, there is no answer, 
            # so output -1
            if num.is_integer() == False:
                return -1

        # correct the off-by-one issue at the very end
        return divid_by_this - 1


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = 6

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