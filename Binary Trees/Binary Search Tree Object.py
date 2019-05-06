"""
    Implementation of a Binary Search Tree
"""


class Node:

    def __init__(self, data):
        self.data_value = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return "<class 'Node'>"


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data_value):
        # Pointer to the root
        pointer = self.root

        # Execute when root, left_child or right_child is empty
        if pointer is None:
            insert_node = Node(data_value)
            self.root = insert_node

        # Execute when left child or right child is empty
        else:
            # Traverse the left child of the root
            if data_value < pointer.data_value:
                # If left child is None
                if pointer.left_child is None:
                    insert_node = Node(data_value)
                    self.root = pointer.left_child
                    self.insert(data_value)
                    pointer.left_child = insert_node
                    self.size += 1
                else:
                    self.root = pointer.left_child
                    self.insert(data_value)
                self.root = pointer

            # Traverse the right child of the root
            else:
                # If right child is None
                if pointer.right_child is None:
                    insert_node = Node(data_value)
                    self.root = pointer.right_child
                    self.insert(data_value)
                    pointer.right_child = insert_node
                    self.size += 1
                else:
                    self.root = pointer.right_child
                    self.insert(data_value)
                self.root = pointer

    def insertion(self, root_value, insertion_value):
        """

        :param root_value: Access to the root of a tree
        :param insertion_value: A given value to delete
        :return: None
        """

        pointer = root_value

        # Return if root is None
        if self.root is None:
            self.root = Node(insertion_value)
            return

        elif insertion_value < pointer.data_value:
            if pointer.left_child is None:
                pointer.left_child = Node(insertion_value)
                self.size += 1
                return
            else:
                self.insertion(pointer.left_child, insertion_value)
        else:
            if pointer.right_child is None:
                pointer.right_child = Node(insertion_value)
                self.size += 1
                return
            else:
                self.insertion(pointer.right_child, insertion_value)

    # def deletion(self, root_value, deletion_value):
    #     """
    #
    #     :param root_value: Access to the root of a tree
    #     :param deletion_value: A given value to delete
    #     :return: Reference to the deletion value
    #     """
    #
    #     pointer = root_value
    #
    #     # Return None if root is empty
    #     if root_value is None:
    #         return
    #
    #     #
    #     else:
    #
    #         if deletion_value < pointer.data_value:
    #             # Check if root node has left child
    #             if pointer.left_child and pointer.data_value == deletion_value:
    #                 # left_child
    #                 left_child = pointer.left_child

    def traversal(self, root_value):
        """

        :param root_value: Access to the root of a tree
        :return: None
        """
        pointer = root_value

        # Return None if not root
        if pointer is None:
            return
        # Process the root value or node value //
        # And return None if node's left and right child are None
        elif pointer.left_child is None and pointer.right_child is None:
            # print(pointer.data_value)
            return
        else:
            # Recursive call on left child's Node value
            self.traversal(pointer.left_child)

            # Printing the root value of every sub-tree
            # print(pointer.data_value)

            # Recursive call on right child's Node value
            self.traversal(pointer.right_child)


tree = BinarySearchTree()


"""
    Insert test
"""
# tree.insert(20)
# tree.insert(10)
# tree.insert(30)
# tree.insert(5)
# tree.insert(35)
# tree.insert(25)
# tree.insert(15)
# tree.insert(40)

"""
    Insertion test - test for recursive insertion
"""

tree_root = tree.root

tree.insertion(tree_root, 20)
tree.insertion(tree_root, 10)
tree.insertion(tree_root, 30)
tree.insertion(tree_root, 5)
tree.insertion(tree_root, 35)
tree.insertion(tree_root, 25)
tree.insertion(tree_root, 15)
tree.insertion(tree_root, 40)


"""
    Traversal test 
    // Printing values Inorder Traversal
    // Given access to the root of a tree
"""
tree.traversal(tree_root)

"""

"""
