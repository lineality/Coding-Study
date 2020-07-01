# https://edabit.com/challenge/SNM5EZ3FePECt2HQn
#
# (User) Problem
# We know / We have: prob  prize  pay
# We don't know / We need: true if prob * prize > pay
# We must / Requirements: name profitable_gamble()
# 3 parameters/arguements
#
# Solution (Product)
# if (function) true, else: False
# both normal and lambda version
# alt: use the whole expression as a boolean

# Normal version 1
def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    else:
        return False


# Normal version 2
def profitable_gamble(prob, prize, pay):
    # This is a boolean: True or False is output
    return prob * prize > pay


# lambda version
# verion 1: using if-else
# profitable_gamble = lambda prob, prize, pay: True if prob * prize > pay else False
#
# verions 2: using just statement as boolean
profitable_gamble = lambda prob, prize, pay: prob * prize > pay
