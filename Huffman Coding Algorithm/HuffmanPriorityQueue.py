"""
    Implementation of a priority queue
"""


class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.Next = None

    def __str__(self):
        return "<class 'Node'>"


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _insert_head(self, char, freq):
        """
        Time complexity - O(1)
        Auxiliary space - O(1)
        Space complexity - O(1)
        :param char: A character value for a Node
        :param freq: A frequency value for a Node
        :return: None
        """
        insert_node = Node(char, freq)

        self.head = insert_node
        self.tail = insert_node

    def _insert_tail(self, node):
        """
        Time complexity - O(1)
        Auxiliary space - O(1)
        Space complexity - O(1)
        :param node: An instance of a Node
        :return: None
        """
        self.tail.Next = node
        self.tail = node

    def enqueue(self, char, freq):
        """
        Time complexity - O(n)
        Space complexity - O(n)
        Auxiliary space - O(1)
        :param char: A character value for a Node
        :param freq: A frequency value for a Node
        :return: None
        """
        if self.head is None:
            self._insert_head(char, freq)
        else:
            insert_node = Node(char, freq)
            if insert_node.freq <= self.tail.freq:
                self._insert_tail(insert_node)
            else:
                pointer = self.head

                if insert_node.freq >= pointer.freq:
                    insert_node.Next = pointer
                    self.head = insert_node
                    self.size += 1
                    return

                while pointer is not None:
                    if insert_node.freq > pointer.Next.freq:
                        insert_node.Next = pointer.Next
                        pointer.Next = insert_node
                        break
                    pointer = pointer.Next

        self.size += 1

    def dequeue(self):
        """
        Time complexity - O(n)
        Space complexity - O(1)
        Auxiliary space - O(1)
        :return: Value with the least frequency in the priority queue
        """
        pointer = self.head
        leaf_node = self.tail
        while pointer is not None:
            if pointer.Next is self.tail:
                pointer.Next = None
                self.tail = pointer
                break
            else:
                pointer = pointer.Next

        self.size -= 1
        return leaf_node


# new_queue = SinglyLinkedList()
# new_queue.enqueue("D", 1)
# new_queue.enqueue("A", 4)
# new_queue.enqueue("M", 3)
# new_queue.enqueue("S", 2)
# new_queue.enqueue("S", 2.4)
# new_queue.enqueue("S", 1.5)
#
# print(new_queue.dequeue())
