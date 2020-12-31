# https://binarysearch.com/
# GGA 2020.12.04
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

        # set local counter to 0 (counting only-children)
        local_counter = 0

        # set cumulative_counter to 0 (counting only-children)
        cumulative_total_counter = 0

        # 1. base case: root is empty
        if not root:
            return 0

        # 2. check children (not recoursive)
        # this updates local_counter (counting only-children)
        if (root.right == None and root.left != None) or (
            root.left == None and root.right != None
        ):
            local_counter += 1

        # 3. recoursive check through tree: \
        # passing results to cumulative_total_counter (counting only-children)
        cumulative_total_counter += (
            local_counter + self.solve(root.right) + self.solve(root.left)
        )

        # return result of step 3
        return cumulative_total_counter


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
