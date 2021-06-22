# for https://binarysearch.com/
# GGA 2020.12.31
"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:

Solution (Feature/Product)

   (Edge cases)




Reflect On, Improvements, Comparisons with other Solutions:

I learned:


"""


class Solution:
    def solve(self, nums):
        pass


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