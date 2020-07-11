# (User's) problem
# We Have:
#    one input integer
#
# We Need:
#    whether that integer is a
#    curzon number: if 1 + 2^int is divisible by 1 + 2*int
#
# We Must:
#    output a boolean: T/F
#    name of function: is_curzon()
#
# Solution (Product)
#     use the expression itself as a boolean (no 'if')
#     use modulus for divisibility
#     ()%()=0
# ALT: use NOT instead of == 0
# ALT: use << instead of ** for exponent


# Normal Version
def is_curzon(input):
    # output True if divisible, else false
    return (1 + 2 ** input) % (1 + 2 * input) == 0


# Lambda Version
# is_curzon = lambda input: not (1 + 2 << input) % (1 + 2 * input)
is_curzon = lambda input: (1 + 2 ** input) % (1 + 2 * input) == 0
