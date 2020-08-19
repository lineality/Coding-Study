# (User's) Problem
# We Have:
#      int
# We Need:
#      from 1 to int as string
# We Must:
#     function name (unclear)
#     str output
#
# Solution (Product)
#     use recusive function to get n factorial


def recursive_factorial(n):
    n = int(n)
    # base case
    if n == 1:
        return print(n, end="")

    else:  # until you reach base case
        recursive_factorial(n - 1)
        return print(n, end="")


# what form is this? (crazy hacker rank...)
if __name__ == "__main__":
    n = int(input())
    recursive_factorial(n)
