# (User's) Problem
# We Have:
#     a year
# We Need:
#     is it a leap year
# We Must:
#     function name
#     boolean output
#
# Solution (Product)
# to check divisibiilty, use notation: not x % 4 which return boolean


# Is a year a leap year? True or False
def is_leap(year_input):

    leap_year_flag = False

    if not year_input % 4:  # if year divisible by 4: yes
        leap_year_flag = True

        if not year_input % 100:  # unless, also divisible by 100: no
            leap_year_flag = False

            if not year_input % 400:  # unless, also divisible by 100: yes
                leap_year_flag = True

    return leap_year_flag
