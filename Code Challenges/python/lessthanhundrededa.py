# Problem (User)
# We know / We have: two numbers
# We need / We don't have: is the sum < 100
# We must / Requirements: function name: less_than_100
#
# Solution (Product)
# 1. if else, one check, is sum < or > 100
# or
# 2. use one boolean expression: result true or false


# # Normal function version:
# # checks if sum of 2 number is less that 100
# def less_than_100(number_1, number_2):
#     if number_1 + number_2 < 100:
#         return True
#     else:
#         return False


# # alt: Lambda version 1
# less_than_100 = lambda a, b: True if (a + b < 100) else False

# # alt: Lambda version 2
# less_than_100 = lambda a, b: a + b < 100
# # or
less_than_100 = lambda number_1, number_2: number_1 + number_2 < 100
