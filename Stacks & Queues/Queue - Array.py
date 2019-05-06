"""
    Implementation of a Queue using an Array
"""


class QueueArray:

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        """

        :param data:
        :return:
        """
        self.queue.insert(0, data)

    def dequeue(self):
        """

        :return:
        """
        return self.queue.pop()

    def peek(self):
        """

        :return:
        """
        return self.queue[-1]

    def is_empty(self):
        """

        :return:
        """

        if len(self.queue) == 0:
            return True
        return False

    def getsize(self):
        """

        :return:
        """
        return len(self.queue)


# Instance of a queue
queue = QueueArray()

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
