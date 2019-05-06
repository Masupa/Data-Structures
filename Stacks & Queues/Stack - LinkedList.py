"""
    Implementation of a Stack using a linked List
"""


class Node:

    def __init__(self, data):
        self.data_ = data
        self.next_ = None


class StackLinkedList:

    def __init__(self):
        self.top_ = None
        self.size = 0

    def push(self, data):
        """
        time-complexity: O(1)
        space-complexity:
        auxiliary-space:
        :param data: The data item to push into the stack
        :return: None
        """

        insert_item = Node(data)

        # Push when the stack is empty
        if self.top_ is None:
            self.top_ = insert_item
        # Push when the stack is not empty
        else:
            insert_item.next_ = self.top_
            self.top_ = insert_item
        # Increase the size
        self.size += 1

    def pop(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Pops and returns the top most item
        """
        pop_item = self.top_

        self.top_ = pop_item.next_
        self.size -= 1

        return pop_item.data_

    def peek(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Returns the top most item
        """

        return self.top_.data_

    def is_empty(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Boolean - True if empty, else false
        """

        if self.size == 0:
            return True
        return False

    def getsize(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: The size of the stack
        """

        return self.size


# Instance of a stack
stack = StackLinkedList()

"""
    Push test
"""
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

"""
    Pop test
"""
print(stack.pop())

"""
    GetSize test
"""
print(stack.getsize())

"""
    Peek test
"""
print(stack.peek())

"""
    Is Empty test
"""
print(stack.is_empty())