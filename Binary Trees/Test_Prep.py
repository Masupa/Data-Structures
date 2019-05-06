class BinarySearchTreeNode:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return "<class 'BinarySearchTreeNode'>"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, root_value, value):
        root_pointer = root_value

        # If the tree is empty
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
        # else the tree is null
        else:
            # Check if the insert value > the root value
            if value >= root_pointer.value:
                # Check if there is no right child
                if root_pointer.right_child is None:
                    root_pointer.right_child = BinarySearchTreeNode(value)
                    return
                # Recursive call on the right child as root
                self.insert(root_pointer.right_child, value)

            # Else if the insert value < the root value
            else:
                # Check if there is a left child
                if root_pointer.left_child is None:
                    root_pointer.left_child = BinarySearchTreeNode(value)
                    return
                # Recursive call on the left child as root
                self.insert(root_pointer.left_child, value)

    # def remove(self, root_value, delete_value):
    #     root_pointer = root_value
    #
    #     # If the tree is empty
    #     if root_pointer is None:
    #         print("Tree is empty")
    #
    #     # If root is delete value
    #     elif delete_value == root_pointer.value:


    def search(self, root_point, search_value):
        root_pointer = root_point

        # Base Case 1 - There is no root
        if root_pointer is None:
            print("Tree is empty")
        # Base Case 2 - Root has no left and right child
        elif root_pointer.left_child is None and root_pointer.right_child is None:
            # Comparison to check search value
            if search_value == root_pointer.value:
                print("Found")
            return
        # Recursive step
        else:
            # Traverse the left subtree in pre-order traversal
            self.search(root_pointer.left_child, search_value)

            # Comparison to check search value
            if search_value == root_pointer.value:
                print("Found")

            # Traverse the right subtree in pre-order traversal
            self.search(root_pointer.right_child, search_value)

    def in_oder_traversal(self, root_point):
        root_pointer = root_point

        # Base Case 1 - There is no root
        if root_pointer is None:
            return
        # Base Case 2 - Root has no left and right child
        elif root_pointer.left_child is None and root_pointer.right_child is None:
            print(root_pointer.value)
            return
        # Recursive step
        else:
            # Traverse the left subtree in pre-order traversal
            self.in_oder_traversal(root_pointer.left_child)

            # Print the root subtree with a left or right child
            print(root_pointer.value)

            # Traverse the right subtree in pre-order traversal
            self.in_oder_traversal(root_pointer.right_child)


tree = BinarySearchTree()

# Root is null at first
root = tree.root

tree.insert(root, 10)

# Root is no longer null
root = tree.root

tree.insert(root, 15)
tree.insert(root, 20)
tree.insert(root, 12)
tree.insert(root, 5)
tree.insert(root, 6)
tree.insert(root, 1)

"""
    Traversal test - Pre-order
"""
tree.in_oder_traversal(root)

"""
    Search test
"""
tree.search(root, 0)
