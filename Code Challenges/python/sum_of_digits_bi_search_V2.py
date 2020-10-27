# https://binarysearch.com/room/stack-smashers-4h7zTJbeDi
# GGA 2020.10.20
#
# User Problem
# You have: a number
# You Need: a sum of the individual digits (e.g. 234 -> 2+3+4)
# You Must: return integer
#
# Solution (Feature/Product)
# v1 Convert to a string
# - Make number into a list of numbers (strings)
# - Converst list of strings into list of integers
# - return sum of list of intergers
#
# v2 use powers
# - count powers of ten
# - isolate and remove powers of ten
# - store in a list
# - sum the list
#
# Edge case?
# one digit or empty input?

# using str()...why not use str()?
class Solution_1:
    def solve(self, num):

        # Make number into a list of numbers (strings)
        numlist_1 = list(str(num))

        # Converst list of strings into list of integers
        numlist_2 = [int(i) for i in numlist_1]

        # return sum of list of intergers
        return sum(numlist_2)


# Sample Test Print
Tom = Solution_1()
print(Tom.solve(456))


# Version 2
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

        # return sum of that list of intergers
        return sum(list_of_numbers)


# Sample Test Print
Tom = Solution()
print(Tom.solve(456))

