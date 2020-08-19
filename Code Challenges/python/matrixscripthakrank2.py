# (User's) Problem
# We Have:
#      input string of scrambled vertical script as though in 2D array
# We Need:
#      reformatted string in legible horizontal english
# We Must:
#     function name (unclear)
#     str output
#     internal symbols and extra spaces removed
#     no if statements (why is this exactly?)
#
# Solution (Product)
#
# the input string will actually look like this:
# '7 3\nTsi\nh%x\ni #\nsM \n$a \n#t%\nir!'
# and the \n is one character
#
# Step 1. traverse scrambled text, get matrix shape
# Step 2. Modify the input string to remove "header"
# Step 3. traverse the input_string in correct sequence
# Step 4. Final Formatting:
# Step 5. split into 3 strings: before_char, chars, and after_char
# Step 6. remove symbols between first and last character
# Step 7. remove extra spaces (leave just 1 space)...only between parameters...
# Step 8. bring pieces back together

import re


def matrixElementsSum(input_string):

    # create variables
    rows_shape = ""
    columns_shape = ""
    counter = 0
    new_string = ""

    # Step 1. traverse scrambled text, get matrix shape

    # Get matrix Shape: Rows
    # go until first " "
    while input_string[counter] != " ":
        rows_shape = rows_shape + input_string[counter]
        counter += 1
    # convert str to int
    rows_shape = int(rows_shape)

    # Get matrix Shape: Columns
    # go until first "\" (because escape character \ is \\)
    counter += 1
    while input_string[counter] != "\n":
        columns_shape = columns_shape + input_string[counter]
        counter += 1
    # convert str to int
    columns_shape = int(columns_shape)

    # Step 2. Modify the input string to remove "header"

    # remove number up to first "\n"
    while input_string[0] != "\n":
        input_string = input_string[1:]

    # remove new line escape characters
    input_string = input_string.replace("\n", "")

    # Step 3. traverse the input_string in correct sequence
    # almost each column
    for column in range(1, columns_shape + 1):
        new_string += input_string[column - 1]

        # for ~each row (-1)
        for row in range(1, rows_shape):
            new_string += input_string[column + (columns_shape * row) - 1]

    alpha_list = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"""
    alpha_list = list(alpha_list)

    symbol_list = """!#$%&'()*+,-./\\:;<=>?@[]^_`"{|}~"""
    symbol_list = list(symbol_list)

    # Step 4. Final Formatting:
    # 1. get paramters of first and last character
    characters = []
    symbols = []

    # 2. split into 3 strings: before_char, chars, and after_char
    string_before_alphanumerics = ""
    string_of_alphanumerics = ""
    string_after_alphanumerics = ""

    string_of_alphanumerics = new_string

    # fix this...
    # start with front, find symbols before alphanumerics
    finder_counter = 0
    while string_of_alphanumerics[finder_counter] not in alpha_list:
        string_before_alphanumerics = (
            string_before_alphanumerics + string_of_alphanumerics[finder_counter]
        )
        string_of_alphanumerics = string_of_alphanumerics[1:]

    # find back portion with, find symbols after alphanumerics
    finder_counter = 1
    while string_of_alphanumerics[-finder_counter] not in alpha_list:
        string_after_alphanumerics = (
            string_after_alphanumerics + string_of_alphanumerics[-finder_counter]
        )
        string_of_alphanumerics = string_of_alphanumerics[:-1]

    # reverse
    string_after_alphanumerics = string_after_alphanumerics[::-1]

    # 4. remove symbols between first and last character
    string_of_alphanumerics = re.sub(r"[^\w]", " ", string_of_alphanumerics)

    # 5. remove extra spaces (leave just 1 space)...only between parameters...
    string_of_alphanumerics = string_of_alphanumerics.replace("  ", " ")

    # 6. bring pieces back together
    new_string = (
        string_before_alphanumerics
        + string_of_alphanumerics
        + string_after_alphanumerics
    )

    return new_string


# mm = '7 3\nTsi\nh%x\ni #\nsM \n$a \n#t%\nir!'
# matrixElementsSum(mm)
