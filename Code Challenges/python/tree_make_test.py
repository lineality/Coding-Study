# pre-defined Tree Class
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree_diagram(s)
tree_diagram_list = [0, [4, None, None], [2, [1, [3, None, None], None], None]]

tree_diagram_list = [1, [4, None, None], [2, None, None]]

# tree_diagram_list = [4, None, None]


# recoursive function to made a node
def fill_tree(place_holder_node, tree_diagram_list):

    # Step 1: Value of Node
    # set the value of the node = the first number in the list
    place_holder_node.val = tree_diagram_list[0]

    # Step 2: Left Child
    # if the next item is None
    if tree_diagram_list[1] is None:
        # say the left child node is None
        place_holder_node.left = None

    else:
        # made a node
        left_child_node = Tree()
        # set the left child node as that node
        place_holder_node.left = left_child_node
        # fill in the children of that node
        fill_tree(left_child_node, tree_diagram_list[1])

    # Step 3: Left Child
    # if the next-next item is None
    if tree_diagram_list[2] is None:
        # say the right child node is None
        place_holder_node.right = None
    else:
        # made a node
        right_child_node = Tree()
        # set the right child node as that node
        place_holder_node.right = right_child_node
        # fill in the children of that node
        fill_tree(right_child_node, tree_diagram_list[2])

    return None


# make root of tree
tree_root = Tree(None)

place_holder_node = tree_root

# fill tree
fill_tree(tree_root, tree_diagram_list)


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


print_tree(tree_root)