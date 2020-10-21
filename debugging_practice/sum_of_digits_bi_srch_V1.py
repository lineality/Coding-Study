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
#
# v2 use powers


class Solution_1:
    def solve(self, num):

        # Make number into a list of numbers (strings)
        numlist_1 = list(str(num))

        # Converst list of strings into list of integers
        numlist_2 = [int(i) for i in numlist_1]

        # return sum of list of intergers
        return sum(numlist_2)


# # sample Print
# Tom = Solution_1()
# print(Tom.solve(456))

# not using str() ...why not use str?
class Solution:
    def solve(self, num):

        # make a variable for counting digits
        count_powers = num

        # set counter at zero
        number_of_digits = 0

        while count_powers > 0:
            count_powers = count_powers // 10
            number_of_digits = number_of_digits + 1

        countdown = number_of_digits - 1

        list_of_numbers = [None] * number_of_digits

        while countdown:

            # isolate digit by dividing by power of 10
            digit = num // (10 ** countdown)

            # add each digit to list
            list_of_numbers[countdown] = digit

            # remove largest digit from number
            num -= digit * (10 ** countdown)

            # decriment counter
            countdown -= 1

        # add the last item to the list
        list_of_numbers[0] = num

        # return sum of that list of intergers
        return sum(list_of_numbers)


# # Sample Test Print
# Tom = Solution()
# print(Tom.solve(456))

