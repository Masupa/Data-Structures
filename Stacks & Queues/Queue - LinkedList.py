"""
    Implementation of a Queue ADT using a Linked List
"""


class Node:

    def __init__(self, data):
        self.data_ = data
        self.next_ = None


class QueueLinkedList:

    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def enqueue(self, data):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :param data: Data item inserted into a Queue
        :return: None
        """

        insert_item = Node(data)

        # Executed if queue is empty
        if self.rear is None:
            self.rear = insert_item
            self.front = insert_item
        # Executed if queue is non-empyt
        else:
            insert_item.next_ = self.rear
            self.rear = insert_item
        # Increasing the size
        self.size += 1

    def dequeue(self):
        """
        time-complexity: O(n - 1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Pops and returns the item at the front
        """

        pointer = self.rear

        while pointer.next_.next_ is not None:
            pointer = pointer.next_

        pop_item = pointer.next_

        pointer.next_ = None
        self.front = pointer

        self.size -= 1

        return pop_item.data_

    def peek(self):
        """
        time-complexity: O(n - 1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Returns the item at the front
        """

        pointer = self.rear

        while pointer.next_.next_ is not None:
            pointer = pointer.next_

        return pointer.next_.data_

    def getsize(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: The size of the queue
        """

        return self.size

    def is_empty(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Boolean - True if empty, else False
        """

        if self.size == 0:
            return True
        return False


# Instance of a queue
queue = QueueLinkedList()

"""
    Enqueue test
"""
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

"""
    Dequeue text
"""
print(queue.dequeue())

"""
    Peek test
"""
print(queue.peek())

"""
    Get size test
"""
print(queue.getsize())

"""
    Is empty test
"""
print(queue.is_empty())
