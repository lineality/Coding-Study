# https://binarysearch.com/

# GGA 2020.10.23
#
# User Problem
# You have: int
# You Need: list of strings
# You Must: count up to that number,
# replace multiples of:
# 3 -> fizz
# 5 -> buzz
# 3 & 5 -> fizzbuzz
#
# Solution (Feature/Product)
# make empty list
# make a list counting up
#
#
#
# Edge cases:
#


# FizzBuzz
# Given an integer n, return a list of integers from 1 to n as strings except for multiples of 3 use “Fizz” instead of the integer and for the multiples of 5 use “Buzz”. For integers which are multiples of both 3 and 5 use “FizzBuzz”.

# ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


# class Solution1:
#     def solve(self, n):

#         # make empty list
#         list_of_str = [None] * n

#         # populate list
#         for i in range(0, n):
#             list_of_str[i] = str(i + 1)

#         # look for 3
#         for i in range(0, n):
#             if not int(i) % 3:
#                 list_of_str[i - 1] = "Fizz"

#         # look for 5
#         for i in range(0, n):
#             if not int(i) % 5:
#                 list_of_str[i - 1] = "Buzz"

#         # look for 3 & 5
#         for i in range(0, n):
#             if (not int(i) % 5) and (not int(i) % 3):
#                 list_of_str[i - 1] = "FizzBuzz"

#         print(list_of_str)


# Tom = Solution1()
# Tom.solve(15)


class Solution:
    def solve(self, n):

        # make empty list
        list_of_str = [None] * (n)

        # populate list with numbers
        for i in range(1, n + 1):
            list_of_str[i - 1] = str(i)

            # look for 3 & 5
            if (not int(i) % 5) and (not int(i) % 3):
                list_of_str[i - 1] = "FizzBuzz"
                continue

            # look for 3
            if not int(i) % 3:
                list_of_str[i - 1] = "Fizz"

            # look for 5
            if not int(i) % 5:
                list_of_str[i - 1] = "Buzz"

        return list_of_str


Tom = Solution()
print(Tom.solve(15))


# alt notes:
# [("Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0)) or str(n) for n in range(1, n + 1)]

# class Solution:
# def solve(self, n):
# return [
# "FizzBuzz"
# if i % 15 == 0
# else "Buzz"
# if i % 5 == 0
# else "Fizz"
# if i % 3 == 0
# else str(i)
# for i in range(1, n + 1)
# ]
