# code works in terminal but not accepted by site

# (User's) Problem
# We have:
#     input string
# We need:
#    output as lower case in single quotes plus other text
#    e.g. shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'
# We must:
#    function named shhh
#    account for null input
#
# Solution (Product)
# use str.lower(), str.upper()
# which are build into python (no added packages/libraries)
# note: strings are not mutible
# use f-string to mix variables and fixed text
# note: unput must be put in, in quotes
# note: maybe should be made to handle various input types
# note: the 'capitalize' function vs. (upper, lower) will automatically handle
# the empty input

# # f-string version
# def shhh(string0):
#     if len(string0) == 0:
#         return '"", whispered Edabit.'
#     else:
#         # make sure first letter is capitalized
#         string1 = str.upper(string0[0])
#         # make everything after first letter lower case
#         string2 = str.lower(string0[1:])
#         return f'"{string1}{string2}", whispered Edabit.'


# # non f-string version 1
# def shhh(string0):
#     if len(string0) == 0:
# #        return "\"\", whispered Edabit."
#         return "\"\", whispered Edabit."
#     else:
#         # make sure first letter is capitalized
#         string1 = str.upper(string0[0])
#         # make everything after first letter lower case
#         string2 = str.lower(string0[1:])
#         string3 = ", whispered Edabit."
#         # auto-format will change this
#         # string_q = "\""
#         string_q = "\""
#         string_all = string_q + string1 + string2 + string_q + string3
#         return string_all

# non f-string version 2
def shhh(string0):
    string2 = string0.capitalize()
    # return "\"" + string2 + "\"" + ", whispered Edabit."
    return '"' + string2 + '"' + ", whispered Edabit."


# # lambda version 1: does not account for empty input
# shhh = lambda i: f'"{str.upper(i[0])}{str.lower(i[1:])}", whispered Edabit.'
#
# # lambda version 2: if else (works) but one-line long
# lambda <args> : <return value > if <condition> else <return value>
# shhh = lambda i: f'"{str.upper(i[0])}{str.lower(i[1:])}", whispered Edabit.' if len(i) != 0 else '"", whispered Edabit.'
#
# # lambda version 3:
# shhh = (
#     lambda i: f'"{str.upper(i[0])}{str.lower(i[1:])}", whispered Edabit.'
#     if len(i) != 0
#     else '"", whispered Edabit.'
# )
# lambda version 4:
# shhh = lambda i: "\"" + i.capitalize() + "\"" + ", whispered Edabit."
shhh = lambda i: '"' + i.capitalize() + '"' + ", whispered Edabit."
