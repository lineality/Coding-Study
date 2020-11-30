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
    def solve(self, num_list):

        # get smallest number fro list
        check_this_divisor = min(num_list)

        # flag
        boolean_result = False

        # check each item in list and decriment
        while check_this_divisor != 1:
            # check each item in list
            boolean_result = all(not element % check_this_divisor for element in num_list)

            # if all numbers are divisible -> that's your answer!
            if boolean_result == True:
                break

            # inspection
            print(check_this_divisor)
            print(boolean_result)

            check_this_divisor -= 1

        return check_this_divisor


class Solution_2:
    def solve(self, nums):
        pass


# Sample Print Solution

test_input = [6,9,12]

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