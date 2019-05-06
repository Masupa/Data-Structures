"""
    Implementation of Singly Linked Lists, recursively
"""


class SinglyLinkedListNode:

    def __init__(self, data):
        self.Data = data
        self.Next = None

    def __str__(self):
        return "<class Singly-Linked-List-Node>"


class SinglyLinkedList:

    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Size = 0

    def append(self, value):
        """

        :param value: A value to insert in the List
        :return: None
        """
        append_node = SinglyLinkedListNode(value)

        # Linked List is empty
        if self.Head is None:
            self.Head = append_node
            self.Tail = append_node

        # Linked List is not empty
        # // Given access to the Tail
        else:
            self.Tail.Next = append_node
            self.Tail = append_node

        # Increase the size of the List
        self.Size += 1

    def insert_at_position(self, value, position):
        """

        :param value: A value to insert in the List
        :param position: The position at which the value is intended in insertion
        :return: None
        """

        insert_node = SinglyLinkedListNode(value)

        # Linked list is empty
        if self.Head is None:
            self.Head = insert_node
            self.Tail = insert_node

        # Linked list is not empty
        else:
            # Insertion at first position
            if position == 0:
                insert_node.Next = self.Head
                self.Head = insert_node
                self.Size += 1
            else:
                self.Size -= 1
                self.insert_at_position(value, (position - 1))


# Singly Linked List Object
lst = SinglyLinkedList()

"""
    Testing the "append" method
"""

lst.append(30)
lst.append(25)
lst.append(20)
lst.append(15)
lst.append(10)

"""
    Testing the "insert_at_position" method
"""

# Testing insert at the beginning
lst.insert_at_position(40, 0)

# Testing insert at the end
lst.insert_at_position(40, 6)
