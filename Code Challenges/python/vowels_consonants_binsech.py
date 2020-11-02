# https://binarysearch.com/
#
# GGA 2020.10.23
#
# User Problem
# You have:
# You Need:
# You Must:
#
# Solution (Feature/Product)
# separate vowels and consonants
# sort each
# recombine
#
#
# Edge cases:
#
# Input/Output Example:
# Vowels and Consonants Sort
# Given a lowercase alphabet string s, return a string with all
# the vowels of s in sorted order followed by all
# the consonants of s in sorted order.
# Note: vowels are ["a", "e", "i", "o", "u"] and
# consonants are all other characters.
# Constraints
# n ≤ 100,000 where n is the length of s
# Example 1
# Input
# s = "decalin"
# Output
# "aeicdln"


class Solution:
    def solve(self, input_string):
        # make  variables
        vowel_list = ["a", "e", "i", "o", "u"]
        vowels_in_string = ""
        consonants_in_string = ""

        # iterate through input_string
        for i in input_string:
            # if the string is a vowel, add to vowel_list
            if i in vowel_list:
                vowels_in_string += i
            # if the string is not a vowel, add to vowel_list
            else:
                consonants_in_string += i

        # # sort
        # vowels_in_string = sorted(vowels_in_string)
        # consonants_in_string = sorted(consonants_in_string)

        # return "".join(vowels_in_string + consonants_in_string)
        return "".join(sorted(vowels_in_string) + sorted(consonants_in_string))


# Sample Print Solution & How Long to Run

import time

start = time.time()

Tom = Solution()
print("\nOutput =", Tom.solve("decalin"))

print("Run Time = ", time.time() - start)


class Solution_2:
    def solve(self, s):
        vowels = ["a", "e", "i", "o", "u"]
        return "".join(sorted(s, key=lambda x: (x not in vowels, x)))


# Sample Print Solution & How Long to Run

import time

start = time.time()

Tom = Solution_2()
print("\nOutput =", Tom.solve("decalin"))

print("Run Time = ", time.time() - start)