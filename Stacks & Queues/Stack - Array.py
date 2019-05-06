"""
    Implementation of a Stack ADT using an Array
"""

"""
    Play field - Experiencial file to play around the data types
"""


class StackArray:

    def __init__(self):
        self.stack = list()

    def push(self, data):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :param data: Data item to push into the stack
        :return: None
        """

        self.stack.append(data)

    def pop(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Pops and returns the top most data item in the stack
        """

        return self.stack.pop()

    def peek(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Returns the top most data item in the stack
        """

        return self.stack[-1]

    def is_empty(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Boolean - True if empty, else false
        """

        if len(self.stack) == 0:
            return True
        return False

    def getsize(self):
        """
        time-complexity: O(1)
        space-complexity: O(1)
        auxiliary-space: O(1)
        :return: Size of the stack
        """

        return len(self.stack)


# Instance of a stack
stack = StackArray()

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
stack.pop()

"""
    Peek test
"""
print(stack.peek())

"""
    Is Empty test
"""
print(stack.is_empty())

"""
    Get size test
"""
print(stack.getsize())
