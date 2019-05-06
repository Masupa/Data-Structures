"""
    Python field to test around any implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next_ = None

    def __str__(self):
        return "<class 'Node'>"


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def insert_end(self, data):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :param data: Insertion data for node into list
        :return: None
        """
        insert_head = Node(data)

        # Insertion when the list is empty
        if self.head is None:
            self.head = insert_head
            self.tail = insert_head
        # Insertion when the list is not empty
        else:
            self.tail.next_ = insert_head
            self.tail = insert_head

        # Increase the size of the list
        self.size += 1

    def insert_position(self, position, data):
        """
        time-complexity: O(n) where n is the number of items in the list
        space-complexity: O(1)
        auxiliary-space: O(1)
        :param position: Position to insert Node (head - 0, and so on)
        :param data: Insertion data for node into list
        :return:
        """

        insert_node = Node(data)

        if position > self.size:
            print("Invalid index")
            return

        elif position == self.size:
            self.tail = insert_node

        # Checking if position is head
        elif position == 0:
            insert_node.next_ = self.head
            self.head = insert_node
        else:
            pointer = self.head
            position_counter = 0
            while pointer is not None:
                if position == (position_counter + 1):
                    insert_node.next_ = pointer.next_
                    pointer.next_ = insert_node
                    self.size += 1
                    return
                position_counter += 1
                pointer = pointer.next_

        self.size += 1

    def remove(self, data):
        """
        time-complexity: O(n)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :param data: Data node intended to be deleted
        :return: None
        """

        # Delete node is the head
        if self.head.value is data:
            self.head = self.head.next_
            self.size -= 1
            return
        else:
            pointer = self.head
            while pointer is not None:
                delete_node = pointer.next_
                if pointer.next_.value == data:
                    pointer.next_ = delete_node.next_
                    delete_node.next_ = None
                    self.size -= 1

                    # Making the last node the tail
                    if pointer.next_ is None:
                        self.tail = pointer

                    return
                pointer = pointer.next_

        return "Value not in the list"

    # def remove_position(self, position, data):
    #     """
    #     time-complexity:
    #     space-complexity:
    #     auxiliary-space:
    #     :param position: The position of value to delete
    #     :param data: Data node intended to be deleted
    #     :return: None
    #     """

        # If head is

    def __str__(self):
        return "<class 'Singly Linked List'>"


# Singly Linked List Object
linked_list = SinglyLinkedList()

"""
    Insert end test
"""
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)

"""
    Insert at position test
"""
# linked_list.insert_position(0, 0)
# linked_list.insert_position(1, 0.5)
# linked_list.insert_position(3, 2.5)
# linked_list.insert_position(7, 4.5)

""" 
    Delete test
"""
# linked_list.remove(1)
# linked_list.remove(3)
linked_list.remove(4)
