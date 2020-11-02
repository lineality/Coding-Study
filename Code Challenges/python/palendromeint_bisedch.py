# https://binarysearch.com/
#
# GGA 2020.11.02
#
# User Problem
# You have: an int
# You Need: are digits palendrome
# You Must: dont' use str
#
# Solution (Feature/Product)
#
# Edge cases:
#
# Input/Output Example:
#

# NOT using str() ...why not use str?
class Solution:
    def solve(self, num):

        # make a variable for counting digits
        count_powers = num

        # set counter at zero
        number_of_digits = 0

        # use a while loop to count how many digits there are
        # by dividing by 10 repeatedly
        while count_powers > 0:
            # reduce count_powers by power of 10, by dividing by 10
            count_powers = count_powers // 10
            # increment the digit counter, each time count_powers is > 0
            number_of_digits = number_of_digits + 1

        # set new variable
        countdown = number_of_digits - 1

        # create a custome sized list (for each power of 10)
        list_of_numbers = [None] * number_of_digits

        # for each power of ten, isolate that digit
        # add it to the empty list
        # and remove it from the number
        #
        # so 456 // 100 = 4
        # 4 is added to list in the 100's slot
        # 400 removed from the number
        # 56 is ready for the next iteration
        #
        # 56 // 10 = 5
        # 5 is added to the 10's slot
        # 50 is removed from the number
        # 6 remains
        while countdown:

            # isolate digit by dividing by power of 10
            digit = num // (10 ** countdown)

            # add each digit to list
            list_of_numbers[countdown] = digit

            # remove largest digit from number
            num -= digit * (10 ** countdown)

            # decriment counter (move down to next power of 10)
            countdown -= 1

        # add the last remaining number (10's digit) to the list
        list_of_numbers[0] = num

        reversed_int = 0

        # make a reversed number from the reversed list
        for i in range(1, len(list_of_numbers) - 1):
            # making new number: reversed_int
            # iterate through list:
            # multipy number each number by that power of 10
            # add to sum
            reversed_int += list_of_numbers[-(i-1)] * (10 ** i)

        # return sum of that list of intergers
        return reversed_int == list, list_of_numbers, reversed_int


# Sample Print Solution & How Long to Run

import time

start = time.time()

Tom = Solution()
print("\nOutput =", Tom.solve(123))

print("Run Time = ", time.time() - start)