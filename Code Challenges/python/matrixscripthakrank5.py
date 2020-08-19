# works for all but case 6...


import re

# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/

# 1. Get the first of many input strings
# this first input will tell you how many other later inputs there will be
input_string_1 = input()


# 3. Get the matrix shape from that first input
# use regex to strip out everthing except numbers and spaces
#    from input_numbers
# https://www.programiz.com/python-programming/regex
pattern = "\d+"
shape_data = re.findall(pattern, input_string_1)


# 4. Set shape parameters
# based on the first input
rows_shape = int(shape_data[0])
columns_shape = int(shape_data[1])


# 5. Based on rows shape,
# save all the later inputs in an array
input_array = [None] * (rows_shape + 1)

for i in range(1, rows_shape + 1):
    input_array[i] = input()


# 6. remove empty first item
del input_array[0]


# 7. Join the array of mulitple inputs into one input
# first make a variable to put it all in
input_string = ""
# since join doesn't work for HR for some reason, endless surprises
# do it manually: copy each into growing a string
for i in input_array:
    input_string = input_string + str(i)


# 8. traverse the input_string in correct sequence:
# this unscrambles the vertical vs. horizontal order
new_string = ""
for column in range(1, columns_shape + 1):
    new_string += input_string[column - 1]

    # for ~each row (-1)
    for row in range(1, rows_shape):
        new_string += input_string[column + (columns_shape * row) - 1]

# 9. Final Formatting: character sets
# works

# https://www.w3schools.com/python/python_regex.asp
# regex for characters before text
import re

# new_string = "# @"
new_string = "*&%^  &*% The rain  $ 5 in 45 7Spain %*#(#*&%(#*&%#"

# before first alpha (works)
print(new_string, "(before any changes)")

pre = re.findall("^(.*?)[A-Za-z]", new_string)
pre = "".join(pre)
print(pre)

# middle (works)

mid = re.findall("\w\S*(?:\s\S+)?", new_string)
print(mid)
mid = " ".join(map(str, mid))
print(mid)

# after last alpha (works)
post = re.findall("[^A-Za-z]+$", new_string)
post = "".join(post)
print(post)

print(pre + mid + post)

# 15 return results
print(new_string)
