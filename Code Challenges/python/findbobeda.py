# (User's) Problem
# We have:
#     a list of strings (names)
# We Need:
#     the location of a given name (Bob)
# We Must:
#     use function-name: find_bob
#     return "-1" if "Bob" is not in list
#
# Solution (Product)
#     convert to dictionary
#     stop looking when the name is found
# is version1 fastester?

# version 1
def find_bob(name_list):
    # create dictionary
    name_dict = {}
    # convert list to dictionary of items
    for i in range(len(name_list)):
        name_dict[name_list[i]] = i
        # if you found the name, no need to look further: break
        if name_list[i] == "Bob":
            break
    # Does name appear in dictionary?
    if "Bob" in name_dict:
        return name_dict["Bob"]
    else:  # if not...
        return -1


# shorter version:
def find_bob(names):
    return names.index("Bob") if "Bob" in names else -1


# lambda:
find_bob = lambda i: i.index("Bob") if "Bob" in i else -1
