# for https://binarysearch.com/
# GGA 2020.12.31
"""
User Problem
You Have:
You Need:
You Must:

Input/Output Example:

Solution (Feature/Product)

   (Edge cases)




Reflect On, Improvements, Comparisons with other Solutions:

I learned:


"""


# function counting 'only-children' in tree
class Solution:
    def solve(self, root):
        return None


############################
# Functions to Print Output
############################

# Sample Print Solution


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Rewrite Diagram:
1. [ -> Tree( 
2. ] -> )
"""

tree_diagram_list = [0, [4, None, None], [2, [1, [3, None, None], None], None]]

root = Tree(0, Tree(4, None, None), Tree(2, Tree(1, Tree(3, None, None), None), None))


# print whole tree
def print_tree(root):
    # print current node value
    print(root.val)

    # print left child
    if root.left:
        print_tree(root.left)

    # print right child
    if root.right:
        print_tree(root.right)

    return None


# print input tree for inspection
print_tree(root)

# input is the root node
test_input = root

run_test = Solution()
print("\nOutput   =", run_test.solve(test_input))
